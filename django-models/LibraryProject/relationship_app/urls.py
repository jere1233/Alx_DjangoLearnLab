from django.urls import path
from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Redirect root to book list
    path('', RedirectView.as_view(pattern_name='list_books', permanent=False)),

    # Book management
    path('books/', views.list_books, name='list_books'),
    path('books/add/', views.add_book_view, name='add_book'),
    path('books/<int:pk>/edit/', views.edit_book_view, name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book_view, name='delete_book'),

    # Library detail
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # User Authentication
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Dashboard
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
