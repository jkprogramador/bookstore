from django.test import TestCase
from django.urls import reverse, resolve
from .models import Book
from .views import BookListView, BookDetailView

class BookListViewTest(TestCase):

    def setUp(self) -> None:
        self.book1 = Book.objects.create(
            title = 'Harry Potter',
            author = 'JK Rowling',
            price = '25.00',
        )
        self.book2 = Book.objects.create(
            title = 'Python 101',
            author = 'John Doe',
            price = '41.50',
        )
        url = reverse('book_list')
        self.res = self.client.get(url)
    
    def test_status_code(self) -> None:
        self.assertEqual(200, self.res.status_code)
    
    def test_url_resolves_to_correct_view(self) -> None:
        view = resolve('/books/')
        self.assertEqual(BookListView.as_view().__name__, view.func.__name__)
    
    def test_template(self) -> None:
        self.assertTemplateUsed(self.res, 'books/book_list.html')
    
    def test_book_listing(self) -> None:
        self.assertContains(self.res, self.book1.title)
        self.assertContains(self.res, self.book2.title)
    
    def test_does_not_contain_author(self) -> None:
        self.assertNotContains(self.res, self.book1.author)
        self.assertNotContains(self.res, self.book2.author)
    
    def test_does_not_contain_price(self) -> None:
        self.assertNotContains(self.res, self.book1.price)
        self.assertNotContains(self.res, self.book2.price)


class BookDetailViewTest(TestCase):
    def setUp(self) -> None:
        self.book = Book.objects.create(
            title = 'Fishing for Dummies',
            author = 'Jane Doe',
            price = '16.75',
        )
        url = reverse('book_detail', args=[str(self.book.pk)])
        self.res = self.client.get(url)
    
    def test_status_code(self) -> None:
        self.assertEqual(200, self.res.status_code)
    
    def test_url_resolves_to_correct_view(self) -> None:
        view = resolve(f"/books/{str(self.book.pk)}")
        self.assertEqual(BookDetailView.as_view().__name__, view.func.__name__)
    
    def test_template(self) -> None:
        self.assertTemplateUsed(self.res, 'books/book_detail.html')
    
    def test_book_details(self) -> None:
        self.assertContains(self.res, self.book.title)
        self.assertContains(self.res, self.book.author)
        self.assertContains(self.res, self.book.price)
    
    def test_does_not_contain_incorrect_html(self) -> None:
        self.assertNotContains(self.res, 'I should not be here')