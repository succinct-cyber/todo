from django.urls import path
from . import views

urlpatterns = [
    # Add Task
    path('addTask/', views.addTask, name='addTask'),

    # Mark as done
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    
    # Undo
    path('undo/<int:pk>/', views.undo, name='undo'),

    #Edit Task
    path('editTask/<int:pk>/', views.editTask, name='editTask'),

    # Delete Task
    path('deleteTask/<int:pk>/', views.deleteTask, name='deleteTask'),
]