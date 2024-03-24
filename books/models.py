from django.db import models

class Book(models.Model):
    class TypeChoices(models.TextChoices):
        HARDCOVER = "HB", "Твердый переплет"
        PAPERCOVER = "PB", "Мягкий переплет"
        EBOOK = "EB", "Электронная книга"
    title = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField()
    description = models.TextField(default="")
    book_type = models.CharField(max_length=2, choices=TypeChoices.choices, default=TypeChoices.PAPERCOVER)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, unique=True,default="")
    #datetime.datetime(year=1970, month=1, day=1)

    def __str__(self):
        return self.title


