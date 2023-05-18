from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes_view, name="notes"),
    path('note/<int:pk>/', views.get_note, name="get-note"),
    path('add/', views.add_note, name="add-note"),
]
