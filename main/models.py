from django.db import models


class Questboard(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    stars = models.IntegerField()

    def __str__(self):
        return self.name

    def stars_int(self):
        return "\u2B50"*self.stars


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

    def stars_int(self):
        return "\u2B50"*self.stars


class addPerson(models.Model):
    SLOTS = (
        ('Slot 1', 'Slot 1'),
        ('Slot 2', 'Slot 2'),
        ('Slot 3', 'Slot 3')
    )
    name = models.CharField(max_length=70)
    slot = models.CharField(max_length=10, choices=SLOTS)


class addPerson2(models.Model):
    SLOTS = (
        ('Slot 1', 'Slot 1'),
        ('Slot 3', 'Slot 3')
    )
    name = models.CharField(max_length=70)
    slot = models.CharField(max_length=10, choices=SLOTS)


class addPerson1(models.Model):
    SLOTS = (
        ('Slot 2', 'Slot 2'),
        ('Slot 3', 'Slot 3')
    )
    name = models.CharField(max_length=70)
    slot = models.CharField(max_length=10, choices=SLOTS)


class addPerson3(models.Model):
    SLOTS = (
        ('Slot 1', 'Slot 1'),
        ('Slot 2', 'Slot 2')
    )
    name = models.CharField(max_length=70)
    slot = models.CharField(max_length=10, choices=SLOTS)


class addPersonOne(models.Model):
    SLOTS = (
        ('Slot 1', 'Slot 1'),
        ('', ''),
    )
    name = models.CharField(max_length=70)
    slot = models.CharField(max_length=10, choices=SLOTS)


class addPersonTwo(models.Model):
    SLOTS = (
        ('Slot 2', 'Slot 2'),
        ('', ''),
    )
    name = models.CharField(max_length=70)
    slot = models.CharField(max_length=10, choices=SLOTS)


class addPersonThree(models.Model):
    SLOTS = (
        ('Slot 3', 'Slot 3'),
        ('', ''),
    )
    name = models.CharField(max_length=70)
    slot = models.CharField(max_length=10, choices=SLOTS)
