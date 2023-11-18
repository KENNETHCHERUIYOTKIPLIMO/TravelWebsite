from django.db import models


# Create your models here.

class viewForm(models.Model):
    title = models.CharField(max_length=200)
    flightNo = models.IntegerField()
    departureTime = models.DateTimeField()
    timeTaken = models.TimeField()


def __str__(self):
    return self.title


class popular(models.Model):
    country = models.CharField(max_length=200)
    continent = models.CharField(max_length=200)
    days = models.CharField(max_length=200)

    def __str__(self):
        return self.country


class Booking(models.Model):
    firstName= models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    mobileNo= models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    checkIn = models.DateTimeField()
    checkOut = models.DateTimeField()
    adult = models.PositiveIntegerField()
    kid = models.PositiveIntegerField()
    specialRequest = models.CharField(max_length=200)

    def __str__(self):
        return self.firstName