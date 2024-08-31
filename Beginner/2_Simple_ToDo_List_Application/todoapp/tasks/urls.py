from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name=""),
    path('update_task/<str:pk>/', views.updatetask, name="update_task"),
    path('delete_task/<str:pk>/', views.deletetask, name="delete_task"),
]