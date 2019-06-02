from django.db import models

class AndroidPackage(models.Model):
   application = models.TextField()
   package_name = models.TextField()
   package_version_code = models.TextField()
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return "{0} {1}".format(self.package_name, self.package_version_code)