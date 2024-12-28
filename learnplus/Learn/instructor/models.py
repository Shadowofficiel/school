from django.db import models
from django.contrib.auth.models import User
from school.models import Classe, Matiere
from django.utils.text import slugify


# Modèle pour les instructeurs
class Instructor(models.Model):
    user = models.OneToOneField(User, related_name='instructor', on_delete=models.CASCADE)
    contact = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    classe = models.ForeignKey(Classe, related_name='instructor_classe', on_delete=models.CASCADE, null=True)
    photo = models.ImageField(upload_to='images/Instructor')
    bio = models.TextField(default="Votre bio")
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Instructor, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Instructor'
        verbose_name_plural = 'Instructors'

    def __str__(self):
        return self.user.username


# Modèle des affectations matières
class AffectationMatiere(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name="affectations")
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, related_name="affectations")
    date_assigned = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.instructor.user.username} - {self.matiere.nom}"
