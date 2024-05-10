from django.contrib import admin

# Register your models here.
from polls.models import *

admin.site.register(News)
admin.site.register(Category)