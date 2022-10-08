from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Asset(models.Model):
    Name = models.CharField(max_length=20)
    SerialID = models.CharField(max_length=20)
    Description = models.TextField()
    Owner = models.ForeignKey(to=User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Name + ' ' + self.Owner.username

# Asset Model
# Serial ID
# Asset Description
# owner - Foreign Key - User

status = [(1,'Approved'),(2,'Asset collection'),(3,'Asset Review'),(4,'Replaced / Repaired'),(5,'Verified')]

class AssetTicket(models.Model):
    Asset = models.OneToOneField(Asset,on_delete=models.CASCADE)
    status = models.SmallIntegerField(choices=status)
    



