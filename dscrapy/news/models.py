from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=512, blank=True, null=True)
    url = models.URLField()
    pub_date = models.DateTimeField()
    body = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'