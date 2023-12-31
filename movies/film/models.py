from django.db import models


class nav(models.Model):
    name=models.CharField(max_length=20)
    des=models.CharField(max_length=500)
    image=models.ImageField(upload_to='nav')
    def _str_(self):
        return self.name
