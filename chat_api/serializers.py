from rest_framework import serializers
from .models import Chat, Conversations

class ConversationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversations
        fields = ('conversation_id', 'content', 'direction', 'sender', 'created_at')

class ChatSerializer(serializers.ModelSerializer):
    conversations = ConversationsSerializer(many=True, read_only=True)

    class Meta:
        model = Chat
        fields = ('chat_id', 'chat_name', 'created_at', 'conversations')
