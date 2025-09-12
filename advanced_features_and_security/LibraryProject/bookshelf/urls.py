from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Auth
    path("register/", views.register_view, name="register"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),

    # Books & Libraries
    path("books/", views.list_books_view, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    # Role-based views
    path("admin-role/", views.admin_view, name="admin_view"),
    path("librarian-role/", views.librarian_view, name="librarian_view"),
    path("member-role/", views.member_view, name="member_view"),

    # Secured book operations
    path("add_book/", views.add_book, name="add_book"),        # instead of "books/add/"
    path("edit_book/<int:pk>/", views.edit_book, name="edit_book"),  # instead of "books/<pk>/edit/"
    path("delete_book/<int:pk>/", views.delete_book, name="delete_book"),
]
