from django.db import models
from school import models as school_models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Salon(models.Model):
    """Model definition for Salon."""
    nom = models.CharField(max_length=250, null=True)
    classe = models.OneToOneField(
        school_models.Classe, on_delete=models.CASCADE, related_name="class_room", null=True
    )
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    @receiver(post_save, sender=school_models.Classe)
    def create_salon(sender, instance, created, **kwargs):
        """Automatically create a Salon when a Classe is created."""
        if created:
            Salon.objects.create(classe=instance)

    @receiver(post_save, sender=school_models.Classe)
    def save_salon(sender, instance, **kwargs):
        """Save the related Salon when a Classe is updated."""
        instance.class_room.save()

    class Meta:
        """Meta definition for Salon."""
        verbose_name = 'Salon'
        verbose_name_plural = 'Salons'

    def __str__(self):
        """Unicode representation of Salon."""
        return self.nom if self.nom else "Salon sans nom"


class Message(models.Model):
    """Model definition for Message."""
    auteur = models.ForeignKey(User, related_name="auteur_message", on_delete=models.CASCADE)
    message = models.TextField()
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE, related_name="salon")
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)  # Ajout automatique lors de la création
    date_update = models.DateTimeField(auto_now=True)  # Mise à jour automatique à chaque modification

    class Meta:
        """Meta definition for Message."""
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        """Unicode representation of Message."""
        return f"{self.auteur.username}: {self.message[:20]}..." if self.message else f"{self.auteur.username}"


class PrivateMessage(models.Model):
    """Model definition for PrivateMessage."""
    sender = models.ForeignKey(User, related_name="sent_messages", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="received_messages", on_delete=models.CASCADE)
    message = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)  # Ajout automatique lors de la création
    date_update = models.DateTimeField(auto_now=True)  # Mise à jour automatique à chaque modification

    class Meta:
        """Meta definition for PrivateMessage."""
        verbose_name = "Private Message"
        verbose_name_plural = "Private Messages"
        ordering = ['date_add']

    def __str__(self):
        """Unicode representation of PrivateMessage."""
        return f"From {self.sender.username} to {self.receiver.username}: {self.message[:20]}..."
from django.db import models
from school import models as school_models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Salon(models.Model):
    """Model definition for Salon."""
    nom = models.CharField(max_length=250, null=True)
    classe = models.OneToOneField(
        school_models.Classe, on_delete=models.CASCADE, related_name="class_room", null=True
    )
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    @receiver(post_save, sender=school_models.Classe)
    def create_salon(sender, instance, created, **kwargs):
        """Automatically create a Salon when a Classe is created."""
        if created:
            Salon.objects.create(classe=instance)

    @receiver(post_save, sender=school_models.Classe)
    def save_salon(sender, instance, **kwargs):
        """Save the related Salon when a Classe is updated."""
        instance.class_room.save()

    class Meta:
        """Meta definition for Salon."""
        verbose_name = 'Salon'
        verbose_name_plural = 'Salons'

    def __str__(self):
        """Unicode representation of Salon."""
        return self.nom if self.nom else "Salon sans nom"


class Message(models.Model):
    """Model definition for Message."""
    auteur = models.ForeignKey(User, related_name="auteur_message", on_delete=models.CASCADE)
    message = models.TextField()
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE, related_name="salon")
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)  # Ajout automatique lors de la création
    date_update = models.DateTimeField(auto_now=True)  # Mise à jour automatique à chaque modification

    class Meta:
        """Meta definition for Message."""
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        """Unicode representation of Message."""
        return f"{self.auteur.username}: {self.message[:20]}..." if self.message else f"{self.auteur.username}"


class PrivateMessage(models.Model):
    """Model definition for PrivateMessage."""
    sender = models.ForeignKey(User, related_name="sent_messages", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="received_messages", on_delete=models.CASCADE)
    message = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)  # Ajout automatique lors de la création
    date_update = models.DateTimeField(auto_now=True)  # Mise à jour automatique à chaque modification

    class Meta:
        """Meta definition for PrivateMessage."""
        verbose_name = "Private Message"
        verbose_name_plural = "Private Messages"
        ordering = ['date_add']

    def __str__(self):
        """Unicode representation of PrivateMessage."""
        return f"From {self.sender.username} to {self.receiver.username}: {self.message[:20]}..."
