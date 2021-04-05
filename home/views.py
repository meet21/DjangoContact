from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
def index(request):
    # return HttpResponse("this is home page")
    cont = {
        'var': 'this is set'
    }
    messages.success(request, "this is test message")
    return render(request, 'index.html' , cont)

def about (request):
    # return HttpResponse("this is about page")
    return render(request, "about.html")

def contact (request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact = Contact(name=name, email=email,subject=subject, date=datetime.today())
        contact.save()
        messages.success(request, 'SUCCESS! your form has been successfully submitted and stored in our database')
    return render(request, "contact.html")