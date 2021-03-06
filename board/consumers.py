from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from board.models import Message
import datetime
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        # Display log
        messages = Message.objects.filter(course=self.scope['url_route']['kwargs']['room_name'])
        for i in messages:
            user_day =i.user + ": " + i.created.strftime('%Y-%m-%d %H:%M:%S')
            message = i.message
            self.send(text_data=json.dumps({'message': user_day}))
            self.send(text_data=json.dumps({'message': message}))
            self.send(text_data=json.dumps({'message': ''}))
    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            { 'type': 'chat_message', 'message': message }
        )
        Message.objects.create(
            course = self.scope['url_route']['kwargs']['room_name'],
            user = "ๅ็กใ",
            message = message,
        )
    # Receive message from room group
    def chat_message(self, event):
        # Send message to WebSocket
        messages = Message.objects.filter(course=self.scope['url_route']['kwargs']['room_name'])
        db_message = messages[len(messages)-1]
        user_day = db_message.user + ": " + db_message.created.strftime('%Y-%m-%d %H:%M:%S')
        message = db_message.message
        self.send(text_data=json.dumps({'message': user_day}))
        self.send(text_data=json.dumps({'message': message}))
        self.send(text_data=json.dumps({'message': ''}))
