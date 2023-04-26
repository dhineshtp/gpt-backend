from django.urls import path
from . import views

urlpatterns = [
    path('chats/', views.chat_list, name='chat_list'),
    path('chats/<int:chat_id>/', views.chat_detail, name='chat_detail'),
    path('chats/<int:chat_id>/conversations/', views.conversations_list, name='conversations_list'),
    path('chats/<int:chat_id>/conversations/<int:conversation_id>/', views.conversations_detail, name='conversations_detail'),
]
