# fromw django.shortcuts import render
import os
import uuid

# Django
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import default_storage

# Rest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Serializers
from androidPackageManager.serializers import AndroidPkgSerializer

# Models
from androidPackageManager.models import AndroidPackage

# Constant
package_name = "name"
package_version_code = "versionCode"
post_req_attr = "document"

def file_upload(request, my_file):
    save_path = os.path.join(settings.MEDIA_ROOT, 'uploads', my_file.name)
    path = default_storage.save(save_path, my_file)
    return default_storage.path(path)

def decode_uploaded_file(tmp_path):
   command = 'aapt dump badging ' + tmp_path + ' | grep pack'
   my_cmd = os.popen(command).read()
   array = my_cmd.split(' ')
   store = {package_name: '', package_version_code: ''}
   for cnt in range(0, len(array)):
         tmp = array[cnt].split('=')
         key = tmp[0]
         if tmp and len(tmp) > 1 and key in store:
            value = tmp[1]
            store[key] = value.replace('\'', '')
   if store[package_name] == '' or store[package_version_code] == '':
      return None
   return store

def package_already_exist(package_name, package_version_code):
   app = AndroidPackage.objects.filter(package_name=package_name, package_version_code=package_version_code)
   if len(app) > 0:
      return True
   return False

# Create your views here.

@api_view(['GET', 'POST'])
def model_form_upload(request):
   print(request.method)
   if request.method == 'POST':
      if request.FILES and post_req_attr in request.FILES:
         my_file = request.FILES[post_req_attr]

         # Check extension file
         if not my_file.name.endswith('.apk'):
            return Response("Error: Wrong file extension only send apk file", status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

         # Parse the file uploaded
         tmp_path = file_upload(request, my_file)
         store = decode_uploaded_file(tmp_path)
         if not store:
            default_storage.delete(tmp_path)
            return Response("Error: Erroned file", status.HTTP_422_UNPROCESSABLE_ENTITY)
         
         if package_already_exist(store[package_name], store[package_version_code]):
            default_storage.delete(tmp_path)
            return Response("Error: file information already exist in the database", status.HTTP_409_CONFLICT)

         # Store the file
         file_name = str(uuid.uuid4()) + '.apk'
         path = os.path.join(settings.MEDIA_ROOT, file_name)
         os.rename(tmp_path, path)
         AndroidPackage.objects.create(application="media/" + file_name, package_name=store[package_name], package_version_code=store[package_version_code])
         
         return Response("Save package " + store[package_name] + " in database", status.HTTP_201_CREATED)
      else:
         return Response("Error: Invalid form", status.HTTP_400_BAD_REQUEST)
   elif request.method == 'GET':
      app = AndroidPackage.objects.all()
      serializer = AndroidPkgSerializer(app, many=True)
      return Response(serializer.data, status.HTTP_200_OK)