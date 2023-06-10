from django.contrib import admin
from .models import User, SQLTutorial, Database

# Register your models here.
admin.site.register(User)
admin.site.register(SQLTutorial)
admin.site.register(Database)