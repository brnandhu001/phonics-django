from django.contrib import admin
from import_export.admin import ImportExportModelAdmin #import exportmodeladmin is used to import a file to add object

#pakage install...pip install django-import-export

# Register your models here.

from .models import *


@admin.register(word)#it is used to reg the model to the admin
class WordAdmin(ImportExportModelAdmin): #it for upload a file and make a obj
    pass
