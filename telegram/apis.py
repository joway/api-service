import logging

from rest_framework import viewsets, serializers
from rest_framework.decorators import list_route
from rest_framework.response import Response

logger = logging.getLogger(__name__)


class TelegramMsgSerializer(serializers.Serializer):
    message = serializers.CharField()


class TelegramViewSet(viewsets.GenericViewSet):
    @list_route(methods=['post'], url_path='msg')
    def msg(self, request, *args, **kwargs):
        logger.info(request.data)
        serializer = TelegramMsgSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        return Response(data)
