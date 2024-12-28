from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .models import Salon, Message, PrivateMessage
from django.contrib.auth.models import User


class ChatConsumer(WebsocketConsumer):
    """
    Gère les messages de groupe pour les salons.
    """
def fetch_messages(self, data):
    try:
        salon_id = data.get('classe')  # Récupérer l'ID du salon
        salon = Salon.objects.get(id=salon_id)  # Vérifier l'existence du salon
        messages = Message.objects.filter(salon=salon).order_by('-date_add')[:20]  # Récupérer les messages
        content = {
            'command': 'messages',
            'messages': self.messages_to_json(messages)
        }
        self.send_message(content)  # Envoyer les messages au client
    except Salon.DoesNotExist:
        self.send_error_message("Salon not found")
    except Exception as e:
        self.send_error_message(str(e))

            
def new_message(self, data):
    try:
        print("Données reçues pour 'new_message':", data)
        salon_id = data.get('classe')
        auteur_username = data.get('from')
        message_text = data.get('message')

        salon = Salon.objects.get(id=salon_id)
        auteur = User.objects.get(username=auteur_username)

        message = Message.objects.create(
            auteur=auteur,
            salon=salon,
            message=message_text
        )

        content = {
            'command': 'new_message',
            'message': self.message_to_json(message)
        }
        self.send_chat_message(content)
    except Exception as e:
        print(f"Erreur lors de la création du message : {e}")
        self.send_error_message(f"Error: {e}")



def messages_to_json(self, messages):
    return [self.message_to_json(message) for message in messages]

def message_to_json(self, message):
    return {
        'auteur': message.auteur.username,
        'message': message.message,
        'date_add': message.date_add.strftime('%Y-%m-%d %H:%M:%S')
    }


commands = {
    'fetch_messages': fetch_messages,
    'new_message': new_message,
}

def connect(self):
    self.salon = self.scope['url_route']['kwargs']['classe']  # ID du salon
    self.room_group_name = f"chat_{self.salon}"

    async_to_sync(self.channel_layer.group_add)(
        self.room_group_name,
        self.channel_name
    )
    self.accept()

def disconnect(self, close_code):
    async_to_sync(self.channel_layer.group_discard)(
        self.room_group_name,
        self.channel_name
    )

def send_chat_message(self, message):
    async_to_sync(self.channel_layer.group_send)(
        self.room_group_name,
        {
            'type': 'chat_message',
            'message': message
        }
    )

def chat_message(self, event):
    message = event['message']
    self.send(text_data=json.dumps(message))


class PrivateChatConsumer(WebsocketConsumer):
    """
    Gère les messages privés entre utilisateurs.
    """

    def fetch_private_messages(self, data):
        """Récupère les messages privés entre deux utilisateurs."""
        sender = self.scope['user']
        receiver_id = data.get('receiver')
        if not receiver_id:
            self.send_message({'error': 'Receiver ID is missing'})
            return

        try:
            receiver = User.objects.get(id=receiver_id)
            messages = PrivateMessage.objects.filter(
                sender__in=[sender, receiver],
                receiver__in=[sender, receiver]
            ).order_by('date_add')[:20]
            content = {
                'command': 'private_messages',
                'messages': self.private_messages_to_json(messages)
            }
            self.send_message(content)
        except User.DoesNotExist:
            self.send_message({'error': 'Receiver does not exist'})

    def new_private_message(self, data):
        """Gère l'envoi d'un nouveau message privé."""
        sender = self.scope['user']
        receiver_id = data.get('receiver')
        message_content = data.get('message')

        if not receiver_id or not message_content:
            self.send_message({'error': 'Missing receiver or message content'})
            return

        try:
            receiver = User.objects.get(id=receiver_id)
            private_message = PrivateMessage.objects.create(
                sender=sender,
                receiver=receiver,
                message=message_content
            )
            content = {
                'command': 'new_private_message',
                'message': self.private_message_to_json(private_message)
            }
            self.send_private_chat_message(content)
        except User.DoesNotExist:
            self.send_message({'error': 'Receiver does not exist'})

    def private_messages_to_json(self, messages):
        return [self.private_message_to_json(message) for message in messages]

    def private_message_to_json(self, message):
        return {
            'sender': message.sender.username,
            'receiver': message.receiver.username,
            'message': message.message,
            'date_add': message.date_add.strftime('%Y-%m-%d %H:%M:%S')
        }

    commands = {
        'fetch_private_messages': fetch_private_messages,
        'new_private_message': new_private_message,
    }

    def connect(self):
        """Connexion WebSocket."""
        self.room_name = f"private_{self.scope['user'].id}_{self.scope['url_route']['kwargs']['receiver']}"
        self.room_group_name = f"private_chat_{self.room_name}"

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        """Déconnexion WebSocket."""
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        """Réception des données WebSocket."""
        data = json.loads(text_data)
        command = data.get('command')
        if command in self.commands:
            self.commands[command](self, data)
        else:
            self.send_message({'error': 'Invalid command'})

    def send_private_chat_message(self, message):
        """Envoi d'un message privé à un utilisateur."""
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'private_chat_message',
                'message': message
            }
        )

    def send_message(self, message):
        """Envoi d'un message au client."""
        self.send(text_data=json.dumps(message))

    def private_chat_message(self, event):
        """Réception d'un message privé."""
        message = event['message']
        self.send(text_data=json.dumps(message))