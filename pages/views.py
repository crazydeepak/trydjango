from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request,*args,**kwargs):
    print(args,kwargs)
    print(request.user)
    return render(request,"home.html",{})
    

def contact_view(request,*args,**kwargs):
    return render(request,"contact.html",{})

def about_view(request,*args,**kwargs):
    my_context ={
        "myname":"deepak",
        "mynum":"1234",
        "mylist":[1,2,3,4,5],
        "myhtml":"<h1>Hello World</h1>"

    }
    return render(request,"about.html",my_context)
