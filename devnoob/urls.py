from django.conf.urls import url
from devnoob.views import home
from devnoob.views import cadastro
urlpatterns = [
    url(r'^$',home),
    url(r'^novo/$',cadastro),
]
