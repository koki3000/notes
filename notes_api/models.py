from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.TextField(null= True, blank= True)
    content = models.TextField(null= True, blank= True)
    creation_date = models.DateTimeField(auto_now_add= True)
    update_date = models.DateTimeField(auto_now= True)

    def __str__(self):
        return f'{self.content[0:50]}'