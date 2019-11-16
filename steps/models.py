from django.db import models
import os
from django.conf import settings

class Steps(models.Model):
  number = models.IntegerField()
  title = models.CharField(max_length=120)
  description = models.TextField()
  icon = models.ImageField(upload_to=os.path.join(settings.MEDIA_ROOT, 'images/'), null=True)

  def _str_(self):
    return self.title
