from django.db import models
from django.conf import settings
from django_bleach.models import BleachField
from django.urls import reverse

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

    class Meta:
        verbose_name_plural = "Posts"

    def __str__(self):
        return (f"User: {self.user}\n"
                f"Post: {self.body[:30]}...\n"
                f"Edited by: {self.edited_by if self.edited_by else 'N/A'}\n"
                f"Created: {self.created_date.strftime('%d-%m-%Y %H:%M')}\n"
                f"Last Edited: {self.last_edited_date.strftime('%d-%m-%Y')}")

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'post_id': self.id})


class Comment(models.Model):
    """
    A comment model to add comments to club notices
    """

    post = models.ForeignKey(Posts, related_name='comments',
                             on_delete=models.RESTRICT)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                               on_delete=models.SET_NULL)
    body = BleachField(blank=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.created_date}'
