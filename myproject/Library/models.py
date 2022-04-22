from django.db import models

# Create your models here.

class Book(models.Model):
    BookId=models.AutoField(primary_key=True)
    BookName=models.CharField(max_length=100)
    BookType=models.CharField(max_length=20)
    BookPrice=models.FloatField()
    BookImage=models.ImageField(upload_to="bookimages/",default="No-Image.png")

    def __str__(self):
        return f"{self.BookName}"