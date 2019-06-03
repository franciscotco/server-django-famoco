from rest_framework import serializers

from androirPackageManager.models import AndroidPackage

class AndroidPkgSerializer(serializers.ModelSerializer):
   class Meta:
      model = AndroidPackage
      fields = '__all__'