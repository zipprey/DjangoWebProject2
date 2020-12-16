"""
Definition of urls for DjangoWebProject2.
"""

from datetime import datetime
from products import views
from django.conf.urls import url
import django.contrib.auth.views
from django.contrib.auth.views import LoginView, LogoutView

import app.forms
import app.views

    # Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
import products.views

urlpatterns = [
    # Examples:
    #url(r'^$', app.views.home, name='home'),
    url(r'^product/(?P<product_id>\w+)/$', products.views.product, name='product'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()