

---

### ✅ 4. `delete.md`

```markdown
# Delete Operation

```python
from bookshelf.models import Book

# Retrieve and delete the book instance
retrieved_book = Book.objects.get(title="Nineteen Eighty-Four")
retrieved_book.delete()

# Confirm deletion
print(Book.objects.all())
