from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name=""),
    path('update_task/<str:pk>/', views.updatetask, name="update_task")
]