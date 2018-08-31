from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=225)
    pub_date = models.DateTimeField(editable=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

