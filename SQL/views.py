from django.shortcuts import render
from .models import SQLTutorial

# Create your views here.
def index(request):
    return render(request, "SQL/inbox.html" , {
        "tutorials": SQLTutorial.objects.all()
    })
