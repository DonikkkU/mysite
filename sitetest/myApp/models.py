from django.db import models

class Task(models.Model):
    title = models.CharField('name', max_length=50)
    task = models.TextField('text')

    def __str__(self):
        return self.title