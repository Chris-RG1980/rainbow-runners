from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Posts(models.Model):
    user = models.ForeignKey(
        User, related_name='posts',
        on_delete=models.DO_NOTHING
    )
    body = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.body} - {self.created}"
