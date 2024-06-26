from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    pub_year = models.PositiveIntegerField(null=True, blank=True)
    genre = models.CharField(max_length=255, null=True)
    isbn = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.title} de {self.author}"

class Reviews(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    review_text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    rating = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )

    def __str__(self):
        return f"Resenha de {self.book} por {self.user}"
