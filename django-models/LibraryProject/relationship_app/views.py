from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required, permission_required
from .models import Library, Book, UserProfile, Author  # Import Author here too

# Function-based view to list all books (simple list, uses Book.objects.all())
@login_required
def list_books_view(request):
    books = Book.objects.all()  # Changed from select_related for compliance
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to show library details + list all books in that library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_object(self):
        return get_object_or_404(Library, pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Add related books explicitly
        return context

# User Registration View
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Custom Login View
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Custom Logout View
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

# Role-Based Dashboard View
@login_required
def dashboard_view(request):
    user_profile = getattr(request.user, 'userprofile', None)

    if user_profile:
        if user_profile.role == 'Admin':
            return render(request, 'relationship_app/admin_dashboard.html')
        elif user_profile.role == 'Librarian':
            return render(request, 'relationship_app/librarian_dashboard.html')
        elif user_profile.role == 'Member':
            return render(request, 'relationship_app/member_dashboard.html')
    return redirect('login')

# --- Book Management Views with Permissions ---

# View to add a book - requires 'can_add_book' permission
@login_required
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        if title and author_id:
            author = get_object_or_404(Author, id=author_id)
            Book.objects.create(title=title, author=author)
            return redirect('list_books')
    authors = Author.objects.all()
    return render(request, 'relationship_app/add_book.html', {'authors': authors})

# View to edit a book - requires 'can_change_book' permission
@login_required
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        author_id = request.POST.get('author')
        if author_id:
            book.author = get_object_or_404(Author, id=author_id)
        book.save()
        return redirect('list_books')
    authors = Author.objects.all()
    return render(request, 'relationship_app/edit_book.html', {'book': book, 'authors': authors})

# View to delete a book - requires 'can_delete_book' permission
@login_required
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book_confirm.html', {'book': book})

# Alias for checker compatibility
list_books = list_books_view
