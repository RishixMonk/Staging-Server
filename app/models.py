from django.db import models


class Info(models.Model):
    imagename = models.CharField('imagename', max_length=50)
    portno = models.IntegerField('portno') 

    def __str__(self):
        return self.imagename
    