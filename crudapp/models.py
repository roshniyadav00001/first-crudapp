from django.db import models
from django.contrib.auth.models import User

class customer(models.Model):
    
    userid= models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    name= models.CharField(max_length= 255)
    email= models.CharField(max_length= 255)
    contact= models.CharField(max_length= 20)
    image= models.ImageField(upload_to='media', null=True)
    entrydate= models.DateField( auto_now_add=True , editable=True)
    
    def __str__(self):
        return self.name
    

    

   
