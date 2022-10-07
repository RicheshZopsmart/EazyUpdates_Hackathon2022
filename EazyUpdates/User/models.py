from django.db import models

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

#from mptt.models import MPTTModel, TreeForeignKey, TreeManager

# class Organization(MPTTModel):
#     name = models.CharField(max_length=255, unique=True)
#     members = models.ManyToManyField(User)
#     parent = TreeForeignKey('self', related_name='children')
#     objects = TreeManager()


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

    

