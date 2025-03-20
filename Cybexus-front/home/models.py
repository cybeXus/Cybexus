from django.db import models

class Formation(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    video = models.FileField(upload_to='videos/', null=True, blank=True)  # Champ pour la vidéo
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
