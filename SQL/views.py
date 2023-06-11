from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import SQLTutorial, Database
from django.db import connection
from django.http import JsonResponse
import json
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from django.template import Template, Context

# Create your views here.
def index(request):
    return render(request, "SQL/inbox.html" , {
        "tutorials": SQLTutorial.objects.all(),
        "content": SQLTutorial.objects.all()
    })

def entry(request, title):
    tutorial = SQLTutorial.objects.get(title=title)  
    content = tutorial.content
    template = Template(content)
    context = Context({})
    rendered_content = template.render(context)

    return render(request, "SQL/inbox.html", {
        "tutorials": SQLTutorial.objects.all(),
        "content": rendered_content
    })

def tryit(request):
    return render(request, "SQL/test.html")

@csrf_exempt
def query(request, query):
    print(query)
    cursor = connection.cursor()
    cursor.execute(query)
    r = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    serialized_data = json.dumps(r)
    data = {'columns': columns, 'data':serialized_data}
    return JsonResponse(data, safe=False)
    
