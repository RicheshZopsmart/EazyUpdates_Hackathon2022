from logging import PlaceHolder
from django.db import models
from django.contrib.auth.models import User
# from mptt.models import MPTTModel, TreeForeignKey, TreeManager
from treebeard.mp_tree import MP_Node
# Create your models here.

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


class Team(models.Model):
    Name = models.CharField(max_length=30)
    Lead = models.ForeignKey(User,on_delete=models.CASCADE)
    
class Mentor(MP_Node):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # Mentor = TreeForeignKey('self',on_delete=models.CASCADE,related_name = 'mentors')
    # parent = models.ForeignKey('self',on_delete=models.CASCADE)
    # TODO: Add __str__ method
    
class extended_user(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="users")
    Email = models.EmailField()
    Mentor = models.ForeignKey(Mentor,on_delete=models.CASCADE,related_name="mentors")
    # Mentor = TreeForeignKey('self',on_delete=models.CASCADE,related_name = 'children')
    Mentee = models.ForeignKey(User,on_delete=models.CASCADE,related_name="mentees")
    Designation=models.CharField(max_length=20)
    YOJ = models.DateField()
    Team = models.ForeignKey(Team,on_delete=models.CASCADE)
    EMPID = models.CharField(max_length=10)

        



# Asset Model
# Serial ID
# Asset Description
# owner - Foreign Key - User

# Asset Mgmt (ticket)
# Ticket ID
# Serial ID
# Owner - FK - User
# Description
# Status - Enum {
# Approval from {{Akshat}}
# Asset collection
# Asset Review By {{Anupam}}
# Replaced / Repair / Collected
# Employee Approval
# }



