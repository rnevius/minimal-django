import sys

from django.conf import settings
from django.urls import path
from django.core.management import execute_from_command_line
from django.http import HttpResponse

settings.configure(
    DEBUG=True,
    ROOT_URLCONF=sys.modules[__name__],
)


def index(request):
    return HttpResponse('<h1>A minimal Django response!</h1>')


urlpatterns = [
    path(r'', index),
]

if __name__ == '__main__':
    execute_from_command_line(sys.argv)
