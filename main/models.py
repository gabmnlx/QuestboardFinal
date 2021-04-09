from django.db import models


class Questboard(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    stars = models.IntegerField()

    def __str__(self):
        return self.name


class Questcard(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    person1 = models.CharField(
        max_length=20, null=True, default="", blank=True)
    person2 = models.CharField(
        max_length=20, null=True, default="", blank=True)
    person3 = models.CharField(
        max_length=20, null=True, default="", blank=True)
    stars = models.IntegerField()
    questboard = models.ForeignKey(
        Questboard, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
