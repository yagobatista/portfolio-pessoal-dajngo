from django.contrib import admin
from devnoob.models import Habilidade
from devnoob.models import Portfolio
from devnoob.models import Caracteristica
from devnoob.models import Gosto
from devnoob.models import Recomendacao
from devnoob.models import Perfil
# Register your models here.

admin.site.register(Habilidade)
admin.site.register(Portfolio)
admin.site.register(Caracteristica)
admin.site.register(Gosto)
admin.site.register(Recomendacao)
admin.site.register(Perfil)
