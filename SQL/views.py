from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import SQLTutorial, Customers
from django.db import connection
from django.http import JsonResponse
import json
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from django.template import Template, Context
from .models import User

# Create your views here.
def index(request):
    tutorial = SQLTutorial.objects.get(title="SQL Home")  
    content = tutorial.content
    template = Template(content)
    context = Context({})
    rendered_content = template.render(context)
    return render(request, "SQL/inbox.html" , {
        "tutorials": SQLTutorial.objects.all(),
        "content": rendered_content,
    })

def entry(request, title):
    tutorial = SQLTutorial.objects.get(title=title)  
    content = tutorial.content
    template = Template(content)
    context = Context({})
    rendered_content = template.render(context)

    return render(request, "SQL/inbox.html", {
        "tutorials": SQLTutorial.objects.all(),
        "content": rendered_content,
        "tutorial_title": tutorial.title
    })

def tryit(request, statement):
    print(statement)
    return render(request, "SQL/tryit.html", {
        "statement": statement
    })

def answer(request, title):
    tutorial = SQLTutorial.objects.get(title=title)  
    answer = tutorial.qizanswer
    return JsonResponse(answer, safe=False)



@csrf_exempt
def query(request, query):
    cursor = connection.cursor()
    cursor.execute(query)
    r = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    serialized_data = json.dumps(r)
    data = {'columns': columns, 'data':serialized_data}
    return JsonResponse(data, safe=False)
    
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "SQL/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "SQL/login.html")
    
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        phone = request.POST["phonenumber"]
        country = request.POST["countries"]
        print(100)
        try:
            user = User.objects.create_user(username=username,email=email,password=password)
            user.user_phone = phone
            user.user_country = country
            print(100)
            user.save()
        except IntegrityError:
            return render(request, "SQL/signup.html", {
                "message": "Username already taken."
            })
        return render(request, "SQL/login.html")
    else:
        print(200)
        return render(request, "SQL/signup.html")
        
def logout_view(request):
    logout(request)
    return render(request, "SQL/login.html")