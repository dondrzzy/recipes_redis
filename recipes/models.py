from django.db import models

# Create your models here.

 
class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Recipe(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
