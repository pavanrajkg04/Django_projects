from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name='Home-page'),
    path('login/', views.login, name='login-page'),
    path('register/', views.register, name='register-page'),
]