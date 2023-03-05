from django.db import models

from django.db import models

class Weather(models.Model):
    Name = models.CharField(max_length=100)
    Date = models.DateTimeField(auto_now_add=True)
    blogTopics=models.CharField(max_length=100)
    blog=models.CharField(max_length=100)


    class Meta:
        db_table="Weather"


