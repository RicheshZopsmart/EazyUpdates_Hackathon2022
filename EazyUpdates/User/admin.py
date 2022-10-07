from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from .models import *

class MyAdmin(TreeAdmin):
    form = movenodeform_factory(Mentor)

admin.site.register(Mentor, MyAdmin)
admin.site.register(Team)
admin.site.register(extended_user)