from django.db import models
from django.conf import settings

# Create your models here.


class Posts(models.Model):
    """
    A posts model to create and edit a post
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='posts_authored',
        on_delete=models.DO_NOTHING
    )
    body = models.TextField()
    edited_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='posts_edited',
        null=True,
        blank=True
    )
    created_date = models.DateTimeField(auto_now_add=True)
    last_edited_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.body} - {self.created}"
