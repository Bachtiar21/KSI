from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=225)
    body = models.TextField()
    email = models.TextField()

    def __str__(self):
        return "{}".format(self.title)
