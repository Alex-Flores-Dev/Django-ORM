"""post views"""
from django.shortcuts import render
from datetime import datetime
posts=[
    {
    'name':'Alex',
    'user':'Cote',
    'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'image':'https://picsum.photos/id/237/200/300',
    },
    {
    'name':'Alex',
    'user':'Cote',
    'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'image':'https://picsum.photos/id/237/200/300',
    }
    ]

# Create your views here.
def list_post(request):

    return  render(request,'index.html',{'posts':posts})
