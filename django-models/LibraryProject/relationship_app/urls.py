from django.urls import path
from django.views.generic import RedirectView
from .views import (
    list_books,  # ✅ now literal
    LibraryDetailView,
    register_view,
    CustomLoginView,
    CustomLogoutView,
    dashboard_view,
    add_book_view,
    edit_book_view,
    delete_book_view,
)

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='list_books', permanent=False)),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    path('register/', register_view, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    path('dashboard/', dashboard_view, name='dashboard'),

    path('books/add/', add_book_view, name='add_book'),
    path('books/<int:pk>/edit/', edit_book_view, name='edit_book'),
    path('books/<int:pk>/delete/', delete_book_view, name='delete_book'),
]
