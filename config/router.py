from rest_framework import routers

from telegram.apis import TelegramViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'telegram', TelegramViewSet, base_name='telegram')
