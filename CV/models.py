from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    Competence = models.CharField(max_length=200)
    langue = models.CharField(max_length=1000)
    internet = models.CharField(max_length=500)
    objectif = models.TextField()
    experience = models.TextField()
    education = models.TextField()
    Projet = models.TextField()
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_added']
