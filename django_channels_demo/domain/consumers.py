import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class PlatformConsumer(WebsocketConsumer):

    group_name = 'platform_coordinates'

    def connect(self):
        # Join room group
        print(self.channel_name)
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        latitude = text_data_json['latitude']
        longitude = text_data_json['longitude']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'location_message',
                'latitude': latitude,
                'longitude':  longitude,
            }
        )

    def location_message(self, event):
        latitude = event['latitude']
        longitude = event['longitude']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'latitude': latitude,
            'longitude':  longitude,
        }))
