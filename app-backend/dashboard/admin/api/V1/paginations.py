from rest_framework.pagination import PageNumberPagination


class UserListPagination(PageNumberPagination):
    page_size = 20
    