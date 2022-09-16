"""djangofiles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from myfiles.views import *
from djangofiles import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('About/',about, name='about'),
    path('Blog/',blog, name='blog'),
    path('Contact/',contact, name='contact'),
    path('Main/',main, name='main'),
    path('Project/',project, name='project'),
    path('Services/',services, name='services'),
    path('Single/',single, name='single')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIAFILES_DIRS)










# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'baza',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1',
        'PORT': '5432',
}
}

