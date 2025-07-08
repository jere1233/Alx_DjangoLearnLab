

---

### ✅ 3. `update.md`

```markdown
# Update Operation

```python
from bookshelf.models import Book

# Retrieve and update the book title
retrieved_book = Book.objects.get(title="1984")
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()

# Print the updated title
print(retrieved_book.title)
