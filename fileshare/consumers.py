import asyncio
import json
from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncWebsocketConsumer, AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from fileshare.models import Comments, Upload


class CommentsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.uuid = self.scope['url_route']['kwargs']['uuid']
        self.group_name = 'chat_%s' % self.uuid

        
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

  
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']
        uuid = text_data_json['uuid']
        print(text_data_json)
        await self.save_db(message, uuid)
        # Send message to room group
        #user = self.scope['user']
        #username = user.username
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )

    
    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))

    @database_sync_to_async
    def save_db(self, message, uuid):
        user = self.scope["user"]
        obj = Upload.objects.get(file_id=uuid)
        obj = Comments.objects.create(file_id=obj, author=user, text=message)
        obj.save()