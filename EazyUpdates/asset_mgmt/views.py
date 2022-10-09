from django.http import HttpResponse
import re
from django.shortcuts import render
import json
from django.utils.decorators import method_decorator

from User.models import extended_user
from .custom_decorator import is_executive,is_admin
from .models import *
from django.core.mail import send_mail
from .forms import *
# Create your views here.

        
def Error(request,err):
    return render(request,"asset_msgmt/error.html",{'error':err})

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
        owner_name = AssetObj.Owner.username
        if asset_action=="return":
            return_reason = request.GET["feedback_ok"]
            AssetTicket.objects.create(status=0,Asset=AssetObj,reason = return_reason,owner = request.user)
            send_mail(
                'Asset Return approval',
                owner_name + 'has raise a request for the asset return.\n Please approve the request.',
                'eazy.updates.no.reply@gmail.com',
                ['manager.eazyupdates@gmail.com'],
                fail_silently=False,
            )
            return Assethome(request)
        else:
            damage_type = request.GET["testimonial"]
            desc_damage = request.GET["feedback_great"]
            AssetTicket.objects.create(status=0,Asset=AssetObj,reason = desc_damage,damagetype=damage_type,owner = request.user)
            send_mail(
                'Asset Replacement approval',
                owner_name + ' has raise a request for the asset replacement.\n\nDamage_Desc: '+ desc_damage +'\ndamage_type: '+damage_type+'\nPlease approve the request.',
                'eazy.updates.no.reply@gmail.com',
                ['manager.eazyupdates@gmail.com'],
                fail_silently=False,
            )
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
    
# is IT ADMIN
def AdminPanel(request):
    xuser = extended_user.objects.get(user = request.user)
    if xuser.Level==2:
        # IT Admin
        assets = Asset.objects.all()    
        Tickets = AssetTicket.objects.filter(Asset__id__in = assets)
        return render(request,"asset_mgmt/admin-panel.html",{'tickets':Tickets})
    elif xuser.Level==1:
        # Executive Level Employee
        tickets = AssetTicket.objects.filter(status = 0)
        return render(request,"asset_mgmt/executive-panel.html",{'tickets':tickets})
    else:
        return Error(request,"You are not Authorized! Contact Executive Admin")

@is_admin
def TakeAction(request,ticketID):
    status = AssetTicket.objects.filter(id = ticketID)[0]
    return render(request,"asset_mgmt/take-action.html",{'status':status})


def UpdateStatus(request,ticketID):
    ticket = AssetTicket.objects.get(id = ticketID).incrementStatus()
    return AdminPanel(request)


def RejectTicket(request, ticketID):
    asset = AssetTicket.objects.get(id = ticketID)
    owner = asset.Asset.Owner
    AssetTicket.objects.filter(id = ticketID).delete()
    send_mail(
        'Ticket Rejected',
        owner.username + ', your ticket is rejected is by your manager.',
        'eazy.updates.no.reply@gmail.com',
        ['employee.eazyupdates@gmail.com'],
        fail_silently=False,
    )
    return AdminPanel(request)
    
def replaceAsset(request,assetID):
    asset = Asset.objects.filter(id = assetID).first
    form  = Asset_replace_form()
    context = {"oldAsset":asset,'form':form}
    return render(request,"asset_mgmt/replace-asset.html",context)
