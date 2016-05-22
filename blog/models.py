from django.db import models
from django.utils import timezone


# Create your models here.

# class Dish
class Dish(models.Model):  # Define a Dish (object)
    author = models.ForeignKey('auth.User', related_name='dishes', null=True)   # me default=3 author einai o admin
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    type = models.IntegerField(default=0)
    categoryA = models.IntegerField(default=0)
    categoryB = models.IntegerField(default=0)
    description = models.TextField()
    photo = models.ImageField(upload_to="media/", null=True, blank=True, default=None)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True,)

    def publish(self):  # function that publishes a Dish
        self.published_date = timezone.now()
        self.save()

    def __str__(self):  # function that returns the name of the Dish
        return self.name

