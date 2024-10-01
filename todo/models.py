from django.db import models


# Create your models here.
class Todo(models.Model):
    name = models.CharField()
    time_date = models.DateTimeField(auto_now_add=True,blank=True)
    is_complete = models.BooleanField(default=False)
