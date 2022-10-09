"""EazyUpdates URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import Home
from asset_mgmt.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name="home"),
    path('assets/',Assethome,name='assets'),
    path('ticket/<int:assetID>',assetRaiseticket,name='raise-ticket'),
    path('create-asset-ticket/',createTicketAPI,name='create-ticket'),
    path('track/<int:ticketID>/',TrackTicket,name="track-ticket"),
    path('admin-panel/',AdminPanel,name='admin-panel'),
    path('take-action/<int:ticketID>/',TakeAction,name='take-action'),
    path('update-ticket-status/<int:ticketID>/',UpdateStatus,name='update-ticket-status'),
    path('reject-ticket/<int:ticketID>/',RejectTicket,name='reject-ticket'),
]
