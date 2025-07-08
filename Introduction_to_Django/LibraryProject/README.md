# LibraryProject 
Got it! Here's the **entire README content**, fully written out, so you can copy-paste **directly** into your `README.md` file, no extra steps:

---

# LibraryProject

This is a Django project created as part of the **ALX Django Learn Lab**. The project demonstrates how to set up a Django development environment, define models, perform CRUD operations using Django ORM, and configure the Django Admin interface.

---

## Project Objectives

* Set up a Django project and development environment
* Create a Django app called `bookshelf`
* Define a `Book` model with the following fields:

  * `title`: CharField (max\_length=200)
  * `author`: CharField (max\_length=100)
  * `publication_year`: IntegerField
* Perform and document CRUD operations using Django ORM
* Register the `Book` model with the Django admin interface
* Customize the admin interface for better data management

---

## Project Setup Steps

### 1. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 2. Install Django

```bash
pip install django
```

### 3. Start a Django project

```bash
django-admin startproject LibraryProject
cd LibraryProject
```

### 4. Start a Django app

```bash
python manage.py startapp bookshelf
```

### 5. Register the app in `LibraryProject/settings.py`

```python
INSTALLED_APPS = [
    'bookshelf',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

### 6. Define the `Book` model in `bookshelf/models.py`

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title
```

### 7. Make and apply migrations

```bash
python manage.py makemigrations bookshelf
python manage.py migrate
```

### 8. Create a superuser

```bash
python manage.py createsuperuser
```

### 9. Register the model in `bookshelf/admin.py`

```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)
```

### 10. Run the development server

```bash
python manage.py runserver
```

Visit the site at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
Visit the admin site at: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## CRUD Operations Performed (Django Shell)

### Create a Book (Documented in `create.md`)

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
```

### Retrieve the Book (Documented in `retrieve.md`)

```python
from bookshelf.models import Book
retrieved_book = Book.objects.get(title="1984")
print(retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)
```

### Update the Book title (Documented in `update.md`)

```python
from bookshelf.models import Book
retrieved_book = Book.objects.get(title="1984")
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
```

### Delete the Book (Documented in `delete.md`)

```python
from bookshelf.models import Book
retrieved_book = Book.objects.get(title="Nineteen Eighty-Four")
retrieved_book.delete()
```

---

## Project Structure

```
LibraryProject/
├── LibraryProject/         # Django project configuration
├── bookshelf/              # App with the Book model
├── db.sqlite3              # SQLite database
├── manage.py               # Django CLI
├── README.md               # Project README
├── create.md               # Contains 'create' operation command and output
├── retrieve.md             # Contains 'retrieve' operation command and output
├── update.md               # Contains 'update' operation command and output
├── delete.md               # Contains 'delete' operation command and output
```

---

## Author

Jeremiah Karanja

---

**Task Completed for ALX Django Intro Project**

---

