from django.contrib.auth.models import AbstractUser
from django.db import models

from src.settings import STATIC_URL, MEDIA_URL


class User(AbstractUser):
    image = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True)

    # metodo para obter a rota absuluta da imagem
    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')
