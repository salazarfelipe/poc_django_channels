from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def send_data_to_socket_group(group_name, event_type, data_to_send):
    channel_layer = get_channel_layer()
    data = dict(type=event_type)
    data.update(**data_to_send)
    async_to_sync(channel_layer.group_send)(
        group_name,
        data
    )
