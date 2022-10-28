from django.urls import path
from .views import HomeView, AddPostView, UpdatePostView, DeletePostView, dashboard

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('update-post/<slug:slug>', UpdatePostView.as_view(), name='edit-post'),
    path('delete-post/<slug:slug>', DeletePostView.as_view(), name='delete-post'),
    path('dashboard/',dashboard, name='dashboard')
]