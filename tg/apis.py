import logging
import os

import telegram
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from rest_framework import viewsets, serializers, status
from rest_framework.decorators import list_route
from rest_framework.response import Response

logger = logging.getLogger(__name__)

global bot
if not settings.DEBUG:
    bot = telegram.Bot(token=os.environ.get('TELEGRAM_TOKEN', 'xxx'))
url_validator = URLValidator()


class TelegramMsgSerializer(serializers.Serializer):
    message = serializers.JSONField()


class TelegramViewSet(viewsets.GenericViewSet):
    @staticmethod
    def _sent_msg(chat_id, message_id, text):
        return bot.sendMessage(
            chat_id=chat_id,
            reply_to_message_id=message_id,
            text=text
        )

    @list_route(methods=['post'], url_path='msg')
    def msg(self, request, *args, **kwargs):
        logger.info(request.data)
        serializer = TelegramMsgSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        message = serializer.data['message']
        text = message['text']

        try:
            url_validator(text)
            self._sent_msg(message['chat']['id'], message['message_id'], text)
            return Response(status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
