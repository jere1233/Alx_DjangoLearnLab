
---

### 📄 **update.md**
```markdown
# Update the title of the Book

```python
from bookshelf.models import Book

# Retrieve the book and update its title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Output
print(book)
# <Book: Nineteen Eighty-Four>
