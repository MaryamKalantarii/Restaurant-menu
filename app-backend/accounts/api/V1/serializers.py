from rest_framework import serializers
from accounts.models import CustomeUser
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from django.shortcuts import get_object_or_404



class RegistrationSerializer(serializers.ModelSerializer):

    """
    Serializer for user registration.

    Fields:
        - email: User's email address.
        - password: Primary password.
        - password_confirm: Confirmation for the primary password (write-only).

    Validation:
        - Ensures both password fields match.
        - Validates password strength using Django's built-in password validator.

    On creation:
        - Removes 'password_confirm' from the validated data.
        - Creates a new user using the custom user model.
    """
    
    password_confirm = serializers.CharField(max_length=20, write_only=True)

    class Meta:
        model = CustomeUser
        fields = ["email", "password", "password_confirm"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attrs):
        attrs = super().validate(attrs)

        if attrs.get("password") != attrs.get("password_confirm"):
            raise serializers.ValidationError({"detail": "گذرواژه ها مطابقت ندارند"})

        try:
            validate_password(attrs["password"])
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"detail": list(e.messages)})

        return attrs

    def create(self, validated_data):
        validated_data.pop("password_confirm")
        return CustomeUser.objects.create_user(**validated_data)


class ResendEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(label=("Email"), write_only=True)

    def validate(self, attrs):
        user = get_object_or_404(CustomeUser, email=attrs.get("email"))
        attrs["user"] = user
        return attrs
    



class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for changing user's password.

    - Validates that new passwords match.
    - Ensures the old password is correct.
    - Checks password strength via Django's validators.
    """

    old_password = serializers.CharField(max_length=128, write_only=True)
    new_password1 = serializers.CharField(max_length=128, write_only=True)
    new_password2 = serializers.CharField(max_length=128, write_only=True)

    def validate(self, attrs):
        request = self.context.get("request")
        user = request.user

        old_pass = attrs.get("old_password")
        new_pass1 = attrs.get("new_password1")
        new_pass2 = attrs.get("new_password2")

        if new_pass1 != new_pass2:
            raise serializers.ValidationError(
                {"new_password2": "New passwords do not match."}
            )

        if not user.check_password(old_pass):
            raise serializers.ValidationError(
                {"old_password": "Old password is incorrect."}
            )

        if old_pass == new_pass1:
            raise serializers.ValidationError(
                {"new_password1": "New password cannot be the same as the old password."}
            )

        # Validate password using Django's built-in validators
        try:
            validate_password(new_pass1, user)
        except exceptions.ValidationError as e:
            raise serializers.ValidationError(
                {"new_password1": list(e.messages)}
            )

        return attrs

    def save(self, **kwargs):
        """
        Sets the new password after all validations pass.
        """
        user = self.context["request"].user
        new_password = self.validated_data["new_password1"]
        user.set_password(new_password)
        user.save()
        return user


class PasswordResetRequestSerializer(serializers.Serializer):
    """
    Serializer for handling password reset requests.

    - Accepts an email field.
    - Validates whether the provided email belongs to a registered user.
    - Raises a validation error if no user is found with the given email.
    """
    email = serializers.EmailField()

    def validate_email(self, value):
        if not CustomeUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("User with this email does not exist.")
        return value


class PasswordResetConfirmSerializer(serializers.Serializer):
    """
    Serializer for confirming and saving a new password.

    - Accepts two password fields: new_password1 and new_password2.
    - Validates that both passwords match.
    - Validates password strength using Django's built-in validators.
    - Saves the new password for the given user instance.
    """
    new_password1 = serializers.CharField(write_only=True)
    new_password2 = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs["new_password1"] != attrs["new_password2"]:
            raise serializers.ValidationError({"detail": "گذرواژه ها مطابقت ندارند."})
        validate_password(attrs["new_password1"])
        return attrs

    def save(self, user):
        user.set_password(self.validated_data["new_password1"])
        user.save()
