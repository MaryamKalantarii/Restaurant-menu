from django.urls import path,include

app_name='menu'

urlpatterns = [
    path("api/V1",include("menu.api.V1.urls")),
   

]