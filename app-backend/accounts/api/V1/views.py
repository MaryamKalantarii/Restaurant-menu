from rest_framework.generics import GenericAPIView, UpdateAPIView, RetrieveAPIView, ListAPIView
from django.http import Http404
from .serializers import (
        RegistrationSerializer,
        ResendEmailSerializer,
        ChangePasswordSerializer,
        PasswordResetConfirmSerializer,
        PasswordResetRequestSerializer,
        UpdateProfileCustomerSerializer,
        GetProfileCustomerSerializer,
        AllProfileCustomerSerializer
)
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.api.V1.tasks import send_email_with_celery
from accounts.models import CustomeUser, Profile
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.permissions import IsAuthenticated
from ..V1.paginations import UserListPagination


class RegistrationView(GenericAPIView):
    """
    Handles user registration.

    - Accepts user email and password.
    - Validates password and confirms match.
    - Creates a new user upon successful validation.
    - Generates JWT access token.
    - Sends email verification asynchronously using Celery.
    """

    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):

        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = get_object_or_404(
                CustomeUser, email=serializer.validated_data["email"]
            )
            token = self.get_tokens_for_user(user)
           
            
            verify_url = f"http://127.0.0.1:8000/accounts/api/V1/is-verified/{token}/"

            send_email_with_celery.delay(
                template="email/email_verification.html",
                subject="Verify Your Account",
                context={"verify_url": verify_url, "user": user.email},
                from_email="maryam@admin.com",
                recipient_list=[user.email]
            )
            return Response({"detail": "ایمیل ارسال شد. لطفا ایمیل خود را بررسی کنید."})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_tokens_for_user(self, user):

        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
    
class IsVerifiedView(GenericAPIView):
    """
    Handles email verification using a JWT token.

    - Extracts the user ID from the provided token in the URL.
    - Retrieves the corresponding user from the database.
    - Sets the user's `is_verified` flag to True.
    - Returns a success message if verification is successful.
    - Returns an error message if the token is invalid or expired.
    """
    def get(self, request, *args, **kwargs):
        try:
            user_data = AccessToken(kwargs.get("token"))
            user_id = user_data["user_id"]
            user = get_object_or_404(CustomeUser, id=user_id)
            user.is_verified = True
            user.save()
            return Response({"detail": "حساب شما با موفقیت تأیید شد"})
        except:
            return Response(
                {
                    "detail": "توکن شما ممکن است منقضی شده باشد یا ساختار آن تغییر کند...",
                    "resend email": "http://127.0.0.1:8000/accounts/api/V1/resend",
                }
            )


class ResendEmailView(GenericAPIView):
    """
    Handles resending the verification email to the user.

    - Accepts user email via POST request.
    - Validates the input using a serializer.
    - Checks if the user's email is already verified.
    - If not verified, generates a new access token.
    - Sends a verification email asynchronously using Celery.
    """
    serializer_class = ResendEmailSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        if user.is_verified:
            return Response({"detail": "ایمیل شما قبلا تایید شده است"})
        

        token = self.get_tokens_for_user(user)
        verify_url = f"http://127.0.0.1:8000/accounts/api/V1/is-verified/{token}/"

        send_email_with_celery.delay(
                template="email/email_verification.html",
                subject="Verify Your Account",
                context={"verify_url": verify_url, "user": user.email},
                from_email="maryam@admin.com",
                recipient_list=[user.email]
            )
            
        return Response({"detail": "ارسال مجدد ایمیل...!"})

    def get_tokens_for_user(self, user):
        """
        Generates a JWT access token for the given user.
        """
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)




class ChangePasswordView(GenericAPIView):
    """
    Handles API endpoint that allows authenticated users to change their password.

    Workflow:
    - Accepts POST requests with 'old_password', 'new_password1', and 'new_password2' fields.
    - Validates the request data via `PasswordChangeSerializer`:
        - Checks if the old password is correct.
        - Ensures the new passwords match.
        - Validates the new password strength and complexity.
    - Updates the user's password upon successful validation.
    - Returns a confirmation message on success.

    Important:
    The view passes the current request to the serializer via the `context` argument
    to allow access to the user instance inside the serializer. This is necessary
    for verifying the old password and associating the password change with the correct user.

    Permissions:
    - Only authenticated users can access this endpoint.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()  # sets new password
        return Response(
            {"detail": "رمز عبور با موفقیت تغییر کرد."},
            status=status.HTTP_200_OK
        )



class PasswordResetRequestView(GenericAPIView):
    """
    Handles the password reset request.

    - Accepts user's email via POST request.
    - Validates if the email exists in the system.
    - Generates a JWT token for the user.
    - Constructs a password reset link containing the token.
    - Sends the reset link via email asynchronously using Celery.
    
    Example usage:
    POST /accounts/api/V1/reset-password/
    {
        "email": "user@example.com"
    }

    If the email is registered, the user will receive a password reset link.
    """
    serializer_class = PasswordResetRequestSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        user = CustomeUser.objects.get(email=email)


        token = RefreshToken.for_user(user).access_token

        reset_url = f"http://127.0.0.1:8000/accounts/api/V1/reset-password-confirm/{token}/"

        send_email_with_celery.delay(
            template="email/password_reset.html",
            subject="Reset Your Password",
            context={"reset_url": reset_url, "user": user.email},
            from_email="maryam@admin.com",
            recipient_list=[email]
        )

        return Response({"detail": "لینک تغییر رمز عبور به ایمیل شما ارسال شد."})

class PasswordResetConfirmView(GenericAPIView):
    """
    Handles password reset confirmation using a JWT token.

    - Accepts a POST request with a valid JWT token in the URL.
    - Extracts the user from the token.
    - Accepts and validates new password data from the request body.
    - Updates the user's password if the token is valid and the input is valid.

    Example endpoint:
    POST /accounts/api/V1/reset-password-confirm/<token>/
    
    Request body:
    {
        "new_password1": "newstrongpass123",
        "new_password2": "newstrongpass123"
    }

    Returns a success message upon successful password reset, or an error
    if the token is invalid or expired.
    """
    serializer_class = PasswordResetConfirmSerializer

    def post(self, request, token):
        try:
            user_data = AccessToken(token)
            user_id = user_data["user_id"]
            user = CustomeUser.objects.get(id=user_id)
        except Exception:
            return Response({"detail": "توکن نامعتبر یا منقضی شده است."}, status=400)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)

        return Response({"detail": "رمز عبور با موفقیت بازنشانی شد."})


class UpdateProfileCustomerAPIView(UpdateAPIView):

    """Update the authenticated user's profile."""

    serializer_class = UpdateProfileCustomerSerializer
    queryset = Profile.objects.select_related("user")
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        try:
            return self.queryset.get(user=self.request.user)
        except Profile.DoesNotExist:
            raise Http404("پروفایل کاربر یافت نشد")


class GetProfileCustomerAPIView(RetrieveAPIView):

    """Retrieve the profile of the authenticated user."""

    queryset = Profile.objects.select_related("user")
    serializer_class = GetProfileCustomerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        try:
            return self.queryset.get(user=self.request.user)
        except Profile.DoesNotExist:
            raise Http404("پروفایل کاربر یافت نشد")


class AllProfileCustomerAPIView(ListAPIView):

    """List all user profiles (admin access only), with search, ordering, and pagination."""
    
    queryset = Profile.objects.select_related("user")
    serializer_class = AllProfileCustomerSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = UserListPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['first_name', 'last_name', 'phone_number', 'user__email']
    