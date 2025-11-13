from django.contrib import admin
from .models import GeneroTextual, Texto, OcorrenciaConector

# Isso faz os modelos aparecerem no painel de admin
admin.site.register(GeneroTextual)
admin.site.register(Texto)
admin.site.register(OcorrenciaConector)