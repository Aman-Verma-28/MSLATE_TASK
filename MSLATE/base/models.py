from django.db import models

# Create your models here.


class UserDetails(models.Model):
    name = models.CharField(max_length=25)
    score = models.IntegerField()
    rank = models.IntegerField(default=1)


class NewUserDetails(models.Model):
    name = models.CharField(max_length=25)
    score = models.CharField(max_length=5)

    def __str__(self):
        return self.name+"-->"+str(self.score)
