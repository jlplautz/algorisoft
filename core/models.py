from django.conf import settings
from django.db import models


class BaseModel(models.Model):
    user_creation = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_creation',
                                      null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user_updated = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_updated',
                                     null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        # abstract = True possibilita a criação da BaseModel em outros modelos (entidades)
        abstract = True
