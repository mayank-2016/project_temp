from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    F_items = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Thing(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class UserConnections(models.Model):
    usr = models.ForeignKey(User)
    thing = models.ForeignKey(Thing)

    def __str__(self):
        return self.usr.name + " likes " + self.thing.name