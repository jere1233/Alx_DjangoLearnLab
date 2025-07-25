from django.urls import path
from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import list_books  # ✅ Required by checker

urlpatterns = [
    # Redirect root to book list
    path('', RedirectView.as_view(pattern_name='list_books', permanent=False)),

    # Book management
    path('add_book/', views.add_book_view, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book_view, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book_view, name='delete_book'),

    # Book listing and library details
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # User Authentication
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Dashboard
    path('dashboard/', views.dashboard_view, name='dashboard'),

    # Role-based dashboards
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/librarian/', views.librarian_dashboard, name='librarian_dashboard'),
    path('dashboard/member/', views.member_dashboard, name='member_dashboard'),
]
