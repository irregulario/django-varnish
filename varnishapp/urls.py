from django.conf.urls import url
from django.conf import settings
from manager import VarnishManager

from varnishapp.views import management

urlpatterns = [
    url(r'', management),
]
