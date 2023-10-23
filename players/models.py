from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=200)


class Man(models.Model):
    name = models.CharField(max_length=200)
    xp = models.IntegerField()
    armor = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name = "men")
