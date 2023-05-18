from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes_view, name="notes"),
    path('note/<int:pk>/', views.get_note, name="get-note"),
    path('note/add/', views.add_note, name="add-note"),
    path('note/update/<int:pk>/', views.update_note, name="update-note"),    
    path('note/delete/<int:pk>/', views.delete_note, name="delete-note"),
]