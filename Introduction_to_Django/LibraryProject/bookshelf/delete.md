
---

### 📄 **delete.md**
```markdown
# Delete the Book instance

```python
from bookshelf.models import Book

# Retrieve the book and delete it
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Check that it is deleted
books = Book.objects.all()
print(list(books))

# Expected Output
# []
