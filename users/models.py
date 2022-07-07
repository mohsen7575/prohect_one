from django.db import models


class Animal(models.Model):
    name = models.CharField(
        max_length=127,
        blank=True,
        null=True,
    )


class Dog(models.Model):
    name = models.CharField(
        max_length=127,
        blank=True,
        null=True,
    )
    animal = models.ForeignKey(
        to=Animal,
        on_delete=models.CASCADE,
    )
