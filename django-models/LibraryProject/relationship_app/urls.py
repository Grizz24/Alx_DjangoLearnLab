from django.urls import path
from .views import list_books_view, LibraryDetailView
from django.contrib import admin
from django.urls import path, include
from .views import register_view, login_view, logout_view, list_books_view, LibraryDetailView


urlpatterns = [
    path('books/', list_books_view, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),  # include app urls
]

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("books/", list_books_view, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
]