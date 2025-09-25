from django.db import models

# The Author model represents a single Author.
# Each Author can have many related Book objects through the ForeignKey
# relationship defined in the Book model.
class Author(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


# The Book model represents a written work.
# Each Book belongs to exactly one Author (many-to-one relationship).
# The ForeignKey creates this relationship.
# related_name="books" allows us to access all books of an author with: author.books.all()

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE,related_name="books"
    )

    def __str__(self):
        return self.title