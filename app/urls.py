from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('apply/', views.apply, name='apply'),
    path('signin/', views.signin, name='signin'),
    path('profile/', views.clientdetails, name='profile'),
    path('success/', views.success, name='success'),  # Added success page URL pattern
]
