from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import SQLTutorial, Database

# Create your views here.
def index(request):
    return render(request, "SQL/inbox.html" , {
        "tutorials": SQLTutorial.objects.all(),
        "content": SQLTutorial.objects.get(title="SQL HOME")
    })

def entry(request, title):
    return render(request, "SQL/inbox.html", {
        "tutorials": SQLTutorial.objects.all(),
        "content": SQLTutorial.objects.get(title=title)
    })

def query(request):
    records = Database.objects.all()
    test = Database.objects.get(customerID=1)
    print(test.customerID)
    return render(request, "SQL/test.html", {
        "records": records
    })

