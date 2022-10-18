from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    person = models.ManyToManyField(Person, related_name="cars")
    # person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="cars")
    name = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self) -> str:
        return self.name
