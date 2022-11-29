from django.db import models

# Create your models here.

class Message(models.Model):
    sno = models.AutoField(primary_key=True)
    content = models.TextField() 
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    
    # def __str__(self):
        # return 'Message from ' + self.sno