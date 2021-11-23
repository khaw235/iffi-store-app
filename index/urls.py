from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index-page"), # Home Page
    path('register', views.userRegistrationPage, name='register'), #User Registeration Page
    path('login', views.userLoginPage, name='login'), #User Login Page
    path('body-measurements', views.bodyMeasurements, name='body-measurements'), #Body Measurements Page
]