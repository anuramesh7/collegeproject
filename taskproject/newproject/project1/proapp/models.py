from django.db import models

class Team(models.Model):
    name1 = models.CharField(max_length=250)
    img1 = models.ImageField(upload_to='pics1')
    des1 = models.TextField()
    def __str__(self):
        return self.name1

