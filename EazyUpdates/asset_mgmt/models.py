from operator import truediv
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Asset(models.Model):
    Name = models.CharField(max_length=20)
    SerialID = models.CharField(max_length=20)
    Description = models.TextField()
    Owner = models.ForeignKey(to=User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Name + ' ' + self.Owner.username + ' ' + str(self.id)
    def get_owner(self):
        return self.Owner

# Asset Model
# Serial ID
# Asset Description
# owner - Foreign Key - User

status = [(0,'Opened'),(1,'Approved'),(2,'Asset Review'),(3,'Replaced / Repaired'),(4,'Verified')]

damage_type = [(0,'physical'),(1,'internal')]
class AssetTicket(models.Model):
    Asset = models.ForeignKey(Asset,on_delete=models.CASCADE)
    status = models.SmallIntegerField(choices=status,default=0)
    reason = models.TextField(max_length=150)
    damagetype = models.CharField(max_length=10)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def incrementStatus(self):
        self.status+=1
        self.save()
    