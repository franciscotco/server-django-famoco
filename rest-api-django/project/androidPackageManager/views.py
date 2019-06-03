# fromw django.shortcuts import render
import os
import uuid

# Django
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Rest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Serializers
from androidPackageManager.serializers import AndroidPkgSerializer

# Models
from androidPackageManager.models import AndroidPackage

def file_upload(request):
    save_path = os.path.join(settings.MEDIA_ROOT, 'uploads', str(request.FILES['document']))
    path = default_storage.save(save_path, request.FILES['document'])
    return default_storage.path(path)

# Create your views here.

@api_view(['GET', 'POST'])
def model_form_upload(request):
   if request.method == 'POST':
      if request.FILES and 'document' in request.FILES:
         tmp_path = file_upload(request)
         myFile = request.FILES['document']
         if not myFile.name.endswith('.apk'):
               return self.form_invalid(form)
         command = 'aapt dump badging ' + tmp_path + ' | grep pack'
         myCmd = os.popen(command).read()
         array = myCmd.split(' ')
         store = {'name': '', 'versionCode': ''}
         for cnt in range(0, len(array)):
               tmp = array[cnt].split('=')
               if tmp and len(tmp) > 1 and tmp[0] in store:
                  store[tmp[0]] = tmp[1].replace('\'', '')
         if store['name'] == '' or store['versionCode'] == '':
               return Response("Error", status.HTTP_201_CREATED) # do stuff
         exist = AndroidPackage.objects.filter(package_name=store['name'], package_version_code=store['versionCode'])
         if len(exist) > 0:
               return Response("Error", status.HTTP_201_CREATED) # do stuff
         print("Exist :", exist)
         filename = str(uuid.uuid4()) + '.apk'
         path = os.path.join(settings.MEDIA_ROOT, filename)
         print("PATH :", path)
         os.rename(tmp_path, path)
         AndroidPackage.objects.create(application="media/" + filename, package_name=store['name'], package_version_code=store['versionCode'])
         return Response("fileName", status.HTTP_201_CREATED)
   elif request.method == 'GET':
      print("YOOOO")
      app = AndroidPackage.objects.all()
      print("APP", app)
      serializer = AndroidPkgSerializer(app, many=True)
      print(serializer)
      return Response(serializer.data)