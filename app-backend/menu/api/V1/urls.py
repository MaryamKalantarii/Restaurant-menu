from django.urls import path
from .views import *  



app_name='api-V1-menu'


urlpatterns = [
    path('menu-items/', MenuItemView.as_view(), name='menu-items'),
    path('categories/', CategoryView.as_view(), name='categories'),
]

