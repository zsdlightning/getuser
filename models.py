from django.db import models

# Create your models here.
class CurrUser(models.Model):
    curr_user = models.CharField(max_length=20)
    def __str__(self):
        return self.curr_user
