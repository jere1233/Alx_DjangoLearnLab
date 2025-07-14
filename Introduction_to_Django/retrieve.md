
---

### 📄 **retrieve.md**
```markdown
# Retrieve the created Book instance

```python
from bookshelf.models import Book

# Retrieve all books
books = Book.objects.all()

# Output
for book in books:
    print(book.title, book.author, book.publication_year)

# Expected Output
# 1984 George Orwell 1949
