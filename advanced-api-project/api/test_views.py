from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book

class BookAPITests(APITestCase):  # Inherits from Django's test framework via unittest

    def setUp(self):
        # Create a test user for authenticated actions
        self.user = User.objects.create_user(username="testuser", password="pass1234")

        # Create a sample book
        self.book = Book.objects.create(
            title="Foundation",
            author="Isaac Asimov",
            publication_year=1951
        )

        # Endpoints
        self.list_create_url = reverse("book-list-create")   # /api/books/
        self.detail_url = reverse("book-detail", kwargs={"pk": self.book.pk})  # /api/books/<id>/

    # ----------------- CRUD TESTS -----------------
    def test_list_books(self):
        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(response.data[0]["title"], "Foundation")

    def test_retrieve_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Foundation")

    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="pass1234")
        data = {"title": "Dune", "author": "Frank Herbert", "publication_year": 1965}
        response = self.client.post(self.list_create_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        data = {"title": "Dune", "author": "Frank Herbert", "publication_year": 1965}
        response = self.client.post(self.list_create_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        self.client.login(username="testuser", password="pass1234")
        data = {"title": "Foundation Updated", "author": "Isaac Asimov", "publication_year": 1951}
        response = self.client.put(self.detail_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Foundation Updated")

    def test_delete_book_authenticated(self):
        self.client.login(username="testuser", password="pass1234")
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # ------------- FILTER / SEARCH / ORDER TESTS -------------
    def test_filter_books_by_author(self):
        response = self.client.get(f"{self.list_create_url}?author=Isaac Asimov")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books_by_title(self):
        response = self.client.get(f"{self.list_create_url}?search=Foundation")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["author"], "Isaac Asimov")

    def test_order_books_by_publication_year(self):
        Book.objects.create(title="Dune", author="Frank Herbert", publication_year=1965)
        response = self.client.get(f"{self.list_create_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Foundation")  # oldest first
