from django.db import models
from django.urls import reverse
import uuid

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, null=False, blank=False)
    author = models.CharField(max_length=200, null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)

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
