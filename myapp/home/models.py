from django.db import models

# Create your models here.

class Students(models.Model):
    name = models.CharField (max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()


class Car(models.Model):
    car_name = models.CharField(max_length=10)
    speed = models.IntegerField(default=50)


    def __str__(self):
        return self.car_name
