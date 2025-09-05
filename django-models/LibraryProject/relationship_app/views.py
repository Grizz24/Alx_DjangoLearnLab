from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library


def list_books_view(request):
    """List all books with their authors using a template."""
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context["books"] = Library.books
        return context
