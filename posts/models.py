from django.db import models
from django.conf import settings
from django_bleach.models import BleachField

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
    body = BleachField(blank=False)
    edited_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='posts_edited',
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )
    created_date = models.DateTimeField(auto_now_add=True)
    last_edited_date = models.DateTimeField(auto_now=True)
    club_notice = models.BooleanField()

    def __str__(self):
        return (f"User: {self.user}\n"
                f"Post: {self.body[:30]}...\n"
                f"Edited by: {self.edited_by if self.edited_by else 'N/A'}\n"
                f"Created: {self.created_date.strftime('%d-%m-%Y %H:%M')}\n"
                f"Last Edited: {self.last_edited_date.strftime('%d-%m-%Y')}")
