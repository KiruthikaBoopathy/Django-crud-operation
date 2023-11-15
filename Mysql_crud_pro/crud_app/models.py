from django.db import models


class stud_table(models.Model):
    name = models.CharField(max_length=255)
    rank = models.IntegerField(default=0)
    status = models.CharField(max_length=255)
