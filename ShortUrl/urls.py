from django.conf.urls import url
from django.contrib import admin
from shorturlapp.views import Index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', Index.as_view())
]
