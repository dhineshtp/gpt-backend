from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ChatSerializer, ConversationsSerializer
from .models import Chat, Conversations

@api_view(['GET', 'POST'])
def chat_list(request):
    if request.method == 'GET':
        chats = Chat.objects.all()
        serializer = ChatSerializer(chats, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def chat_detail(request, chat_id):
    try:
        chat = Chat.objects.get(chat_id=chat_id)
    except Chat.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ChatSerializer(chat)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ChatSerializer(chat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        chat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def conversations_list(request, chat_id):
    try:
        chat = Chat.objects.get(chat_id=chat_id)
    except Chat.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        conversations = chat.conversations.all()
        serializer = ConversationsSerializer(conversations, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ConversationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(chat_id=chat)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def conversations_detail(request, chat_id, conversation_id):
    try:
        chat = Chat.objects.get(chat_id=chat_id)
        conversation = chat.conversations.get(conversation_id=conversation_id)
    except (Chat.DoesNotExist, Conversations.DoesNotExist):
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ConversationsSerializer(conversation)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ConversationsSerializer(conversation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        conversation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
