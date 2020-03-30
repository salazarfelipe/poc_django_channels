from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from .utils import send_data_to_socket_group


class Coordinates(models.Model):
    provider = models.CharField(max_length=150)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Coordinates'
        verbose_name_plural = 'Coordinates'

    def __str__(self):
        """Unicode representation of Coordinates."""
        return self.provider


@receiver(post_save, sender=Coordinates)
def send_coordinate_to_platform_socket(sender, instance, **kwargs):
    print("send_coordinate_to_platform_socket")
    data = dict(
        latitude=instance.latitude,
        longitude=instance.longitude
    )
    send_data_to_socket_group('platform_coordinates', 'location_message', data)
