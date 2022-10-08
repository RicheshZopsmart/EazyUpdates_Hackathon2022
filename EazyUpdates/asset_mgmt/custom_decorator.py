from django.contrib.auth.decorators import user_passes_test
from .models import *
from User.models import *
from django.shortcuts import render

def is_executive(func):
    def _wrapper_(request,*args,**kwargs):
        
        if not request.user.is_anonymous: #checking if user is logged in or not
            try: #try if the user even has data in user_extended model
                xuser = extended_user.objects.get(user=request.user)
                if  xuser!=None and xuser.Level != 1: #if user has executive access
                    return render(request,"asset_mgmt/errors.html",{'error':"You don't have access to this page"})
                return func(request,*args,**kwargs) #basic syntax for decorator also args and kwargs help to handle multiple args passing without error
            except:
                msg = "Some Error Occured, Maybe Your access Level is not updated, Kindly Contact Admin"
                return render(request,"asset_mgmt/errors.html",{'error':msg})

        else:
            msg = "You are not signed in"
            return render(request,"asset_mgmt/errors.html",{'error':msg})
    return _wrapper_

def is_admin(func):
    def _wrapper_(request,*args,**kwargs):
        
        if not request.user.is_anonymous: #checking if user is logged in or not
            try: #try if the user even has data in user_extended model
                xuser = extended_user.objects.get(user=request.user)
                if  xuser!=None and xuser.Level != 2: #if user has IT admin access
                    return render(request,"asset_mgmt/errors.html",{'error':"You don't have access to this page"})
                return func(request,*args,**kwargs) #basic syntax for decorator also args and kwargs help to handle multiple args passing without error
            except:
                msg = "Some Error Occured, Maybe Your access Level is not updated, Kindly Contact Admin"
                return render(request,"asset_mgmt/errors.html",{'error':msg})

        else:
            msg = "You are not signed in"
            return render(request,"asset_mgmt/errors.html",{'error':msg})
    return _wrapper_
