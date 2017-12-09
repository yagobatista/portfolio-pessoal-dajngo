from django.conf.urls import url
from devnoob.views import home
urlpatterns = [
    url(r'^$',home)
]
