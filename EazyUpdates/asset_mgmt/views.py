from django.shortcuts import render

from .models import *
# Create your views here.

def Assethome(request):
    asssetObjs = Asset.objects.filter(Owner = request.user)
    return render(request,'asset_mgmt/index.html',{'assets':asssetObjs})

def assetRaiseticket(request,assetID):
    return render(request,"asset_mgmt/ticket.html",{})
    