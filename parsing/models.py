from django.db import models


class InfoHabrs(models.Model):
    title = models.TextField(unique=True)
    url = models.URLField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


