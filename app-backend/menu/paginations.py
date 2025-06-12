from rest_framework.pagination import PageNumberPagination


class MenuItemPagination(PageNumberPagination):
    page_size = 15
    