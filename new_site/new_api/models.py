from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    id=models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    category=models.CharField(max_length=100)

    def __str__(self):
        return self.category

class Book(models.Model):
    book=models.CharField(max_length=100)
    category_name=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.book


