from django.conf.urls import url, include
from django.contrib import admin
from django.http.response import JsonResponse

from config.router import router


def health(request):
    return JsonResponse({
        'success': True,
    })


urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls, namespace='api')),
    url(r'^healthz/', health),
]
