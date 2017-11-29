from rest_framework import routers

from tg.apis import TelegramViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'tg', TelegramViewSet, base_name='tg')
