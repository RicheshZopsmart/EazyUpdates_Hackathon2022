from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import *
# Create your views here.

def Assethome(request):
    assetObjs = Asset.objects.filter(Owner = request.user)
    raisedTicket = AssetTicket.objects.filter(Asset__id__in = assetObjs)
    ids=[]
    for i in raisedTicket:
        ids.append(i.Asset.id)
    return render(request,'asset_mgmt/index.html',{'assets':assetObjs,'raisedTicket':raisedTicket,'ids':ids})

def assetRaiseticket(request,assetID):
    try:
        asset_action = request.GET["rating"]
        AssetObj = Asset.objects.filter(id=assetID)[0]
        if asset_action=="return":
            return_reason = request.GET["feedback_ok"]
            AssetTicket.objects.create(status=0,Asset=AssetObj,reason = return_reason,owner = request.user)
            return Assethome(request)
        else:
            damage_type = request.GET["testimonial"]
            desc_damage = request.GET["feedback_great"]
            AssetTicket.objects.create(status=0,Asset=AssetObj,reason = desc_damage,damagetype=damage_type,owner = request.user)
            return Assethome(request)
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

def TrackTicket(request,ticketID):
    AssetReq = Asset.objects.filter(id = ticketID)
    Ticket = AssetTicket.objects.filter(Asset__id__in = AssetReq).first
    print("Tickets : ",Ticket)
    return render(request,"asset_mgmt/track-ticket.html",{'ticket':Ticket})
    

            