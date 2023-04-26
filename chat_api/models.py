from django.db import models


# Create your models here.
class Chat(models.Model):
    chat_id = models.BigAutoField(unique=True, primary_key=True)
    chat_name = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.chat_id


class Conversations(models.Model):
    chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='conversations')
    conversation_id = models.BigAutoField(unique=True, primary_key=True)
    content = models.TextField(blank=True)
    direction = models.CharField(
        max_length=255,
        choices=(("outgoing", "outgoing"), ("incoming", "incoming")),
        blank=True,
    )
    sender = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
