from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model # use it to refer to CustomUser model
import uuid

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,)
    title = models.CharField(max_length=200, null=False, blank=False,)
    author = models.CharField(max_length=200, null=False, blank=False,)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False,)
    cover = models.ImageField(upload_to='covers/', blank=True,)

    def __str__(self) -> str:
        """
        Return the title of a book.

        :rtype: str
        """
        return self.title
    
    def get_absolute_url(self) -> str:
        """
        Return the canonical URL for this model.

        :rtype: str
        """
        return reverse('book_detail', args=[str(self.id)])


class Review(models.Model):
    # One-to-many foreign key that links Book to Review
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews',)
    review = models.CharField(max_length=255,)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)

    def __str__(self) -> str:
        """
        Return the review.

        :rtype: str
        """
        return self.review