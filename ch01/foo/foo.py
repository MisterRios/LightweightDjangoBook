import os
import sys

from django.conf import settings

from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse

DEBUG = os.environ.get('DEBUG', 'on') == 'on'

SECRET_KEY = os.environ.get('SECRET_KEY', 9e04!e#&^9myvqxz7xw@06p68diqf#eb^z$6&*_h5xlupv!(^()

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')


settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,g
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)


def index(request):
    return HttpResponse('Hello World')


urlpatterns = (
    url(r'^$', index),
    )


application = get_wsgi_application()


if __name__ == '__main__':
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)