from django.urls import path,include

app_name='accounts'

urlpatterns = [
    path('api/', include('accounts.api.V1.urls')),  
   

]