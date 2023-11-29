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
    images = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=200)
    tt = models.CharField(max_length=200)

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

    # class Srch(models.Model):
    #     place = models.CharField(max_length=200)
    #
    #
    #     def __str__(self):
    #         return self.place
class Plan(models.Model):
    destination= models.CharField(max_length=200)
    travelDates = models.CharField(max_length=200)


    def __str__(self):
        return self.destination


class Home(models.Model):
        city=models.CharField(max_length=200)
        about=models.CharField(max_length=200)

        def __str__(self):
            return self.city