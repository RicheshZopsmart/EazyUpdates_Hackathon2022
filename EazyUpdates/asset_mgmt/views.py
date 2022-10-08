from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import *
from django.core.mail import send_mail
# Create your views here.

def Assethome(request):
    asssetObjs = Asset.objects.filter(Owner = request.user)
    raisedTicket = AssetTicket.objects.filter(owner = request.user)
    ids=[]
    for i in raisedTicket:
        ids.append(i.id)
    return render(request,'asset_mgmt/index.html',{'assets':asssetObjs,'raisedTicket':raisedTicket,'ids':ids})

def assetRaiseticket(request,assetID):
    try:
        asset_action = request.GET["rating"]
        AssetObj = Asset.objects.filter(id=assetID)[0]
        if asset_action=="return":
            return_reason = request.GET["feedback_ok"]
            AssetTicket.objects.create(status=0,Asset=AssetObj,reason = return_reason,owner = request.user)
            send_mail(
                'Asset Return approval',
                '{Name}, {EmployeeId}, has raise a request for the asset return.\n Please approve the request.',
                'sukant.2772001@gmail.com',
                ['sharif.nawaz@zopsmart.com'],
                fail_silently=False,
            )
        else:
            damage_type = request.GET["testimonial"]
            desc_damage = request.GET["feedback_great"]
            AssetTicket.objects.create(status=0,Asset=AssetObj,reason = desc_damage,damagetype=damage_type,owner = request.user)
            send_mail(
                'Asset Replacement approval',
                '{Name}, {EmployeeId}, has raise a request for the asset replacement.\nDamage_Type: ' + damage_type + '\nDamge_description: '+ desc_damage+ '\nPlease approve the request.',
                'sukant.2772001@gmail.com',
                ['sharif.nawaz@zopsmart.com'],
                fail_silently=False,
            )
    except:
        pass
    return render(request,"asset_mgmt/ticket.html",{})

def createTicketAPI(request):
    print("Here")
    if request.method =="POST":
        asset_action = request.POST['asset_action']
        if asset_action=="return":
            return_reason = request.POST['return_reason']
            AssetObj = Asset.objects.filter(id = request.POST["id"])
            AssetTicket.objects.create(Asset = AssetObj)
    a = "done"
    return HttpResponse({json.dumps({'a': a})}, content_type="application/json")

            