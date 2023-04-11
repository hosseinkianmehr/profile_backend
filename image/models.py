from django.db import models

class image(models.Model):
    title = models.CharField(("titel"), max_length=50)
    description = models.TextField(("description"))
    image = models.ImageField(("image"), upload_to='files/%Y/%m/%d/')
    create = models.TimeField(("create post"),  auto_now_add=True)
    update = models.TimeField(("create post"), auto_now=True)
    def __str__(self):
        return 

    def __unicode__(self):
        return 
