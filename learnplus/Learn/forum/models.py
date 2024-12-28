from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.text import slugify
from django.utils.crypto import get_random_string
# Create your models here.


class Sujet(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_sujet')
    cours = models.ForeignKey('school.Cours',on_delete=models.CASCADE,related_name='cours_forum', null=True)
    question = models.TextField()
    titre = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, null=True,  blank=True)

    def save(self, *args, **kwargs):
        self.slug = '-'.join((slugify(self.titre), slugify(self.date_add)))
        super(Sujet, self).save(*args, **kwargs)


    class Meta:
        verbose_name = 'Sujet'
        verbose_name_plural = 'Sujets'

    def __str__(self):
        return self.titre


class Reponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reponse')
    sujet = models.ForeignKey(Sujet, on_delete=models.CASCADE, related_name='sujet_reponse')
    reponse = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # Générer un slug unique basé sur le titre du sujet et un identifiant aléatoire
            base_slug = '-'.join((slugify(self.sujet.titre), slugify(self.date_add)))
            self.slug = f"{base_slug}-{get_random_string(8)}"
        super(Reponse, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Reponse'
        verbose_name_plural = 'Reponses'

    def __str__(self):
        return self.sujet.titre
