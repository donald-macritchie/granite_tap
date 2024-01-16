from django.db import models


class About(models.Model):

    class Meta:
        ordering = ['-title']

    title = models.CharField(max_length=254)
    content = models.TextField()

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __str__(self):
            return self.question

