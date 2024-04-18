from django.db.models.signals import post_delete, post_save
from .models import OrderLineItem


def update_total(sender, instance, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()


post_save.connect(update_total, sender=OrderLineItem)
post_delete.connect(update_total, sender=OrderLineItem)
