from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required, permission_required
from .models import Library, Book, UserProfile, Author

# --- Book List View ---
@login_required
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# --- Library Detail View ---
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_object(self):
        return get_object_or_404(Library, pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context

# --- Registration View ---
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# --- Login / Logout Views ---
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

# --- Dashboard View ---
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

# --- Add Book View ---
@login_required
@permission_required('relationship_app.canaddbook', raise_exception=True)
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

# --- Edit Book View ---
@login_required
@permission_required('relationship_app.canchangebook', raise_exception=True)
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

# --- Delete Book View ---
@login_required
@permission_required('relationship_app.candeletebook', raise_exception=True)
def delete_book_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book_confirm.html', {'book': book})
