from django.contrib import admin
from django.urls import path, include # <--- ADICIONE O 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalogo.urls')), # <--- ADICIONE ESSA LINHA
]