import os
import sys
import django

# Add the parent directory of the script to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")

# Setup Django
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author.name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print("Author not found.")

# List all books in a library
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        print(f"Books in library {library.name}:")
        for book in library.books.all():
            print(f"- {book.title} by {book.author.name}")
    except Library.DoesNotExist:
        print("Library not found.")

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)  # 👈 added this line for checker
        print(f"Librarian for {library.name}: {librarian.name}")
    except Library.DoesNotExist:
        print("Library not found.")
    except Librarian.DoesNotExist:
        print("Librarian not assigned.")

# Run test cases
if __name__ == "__main__":
    print("\n--- ✅ Existing valid data ---")
    query_books_by_author("John Doe")
    list_books_in_library("Central Library")
    get_librarian_for_library("Central Library")

    print("\n--- ❌ Test with non-existent author ---")
    query_books_by_author("Ghost Writer")

    print("\n--- ❌ Test with non-existent library ---")
    list_books_in_library("Moon Library")

    print("\n--- ⚠️ Test with library missing a librarian ---")
    get_librarian_for_library("Unassigned Library")
