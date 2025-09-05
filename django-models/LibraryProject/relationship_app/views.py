from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.http import HttpResponse
from .models import Library

# Create your views here.
from .models import Book

def list_books_view(request):
    """Function-based view to list all books with their authors."""
    books = Book.objects.all()
    if not books:
        return HttpResponse("No books found in the database.")

    # Build a simple text response
    response_text = "List of Books:\n\n"
    for book in books:
        response_text += f"- {book.title} by {book.author.name}\n"

    return HttpResponse(response_text, content_type="text/plain")

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()  # safer than relying on self.object
        context["books"] = Library.books
        return context