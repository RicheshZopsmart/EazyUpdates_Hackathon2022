from logging import PlaceHolder
from django.db import models
from django.contrib.auth.models import User
from treebeard.mp_tree import MP_Node


class Team(models.Model):
    Name = models.CharField(max_length=30)
    Lead = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.Name
    
class Mentor(MP_Node):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
    
#Users
# Email - EmailFIeld
# phone number - PhoneField
# Mentor - User - one to one
# mentee - one to many
# Designation
# Year Of Joining
# Team - One to Many
# Level - 1. Executive / 2. IT Admin /3. Employee
# Emp ID

access_level = [(1,'Executive'),(2,'IT'),(3,'Employee')]

class extended_user(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="users")
    Email = models.EmailField()
    Mentor = models.ForeignKey(Mentor,on_delete=models.CASCADE,related_name="mentors")
    Mentee = models.ForeignKey(User,on_delete=models.CASCADE,related_name="mentees")
    Designation=models.CharField(max_length=20)
    YOJ = models.DateField()
    Team = models.ForeignKey(Team,on_delete=models.CASCADE)
    EMPID = models.CharField(max_length=10)
    Level = models.PositiveSmallIntegerField(choices=access_level,default=3)
    
    def __str__(self):
        return self.user.username

        

