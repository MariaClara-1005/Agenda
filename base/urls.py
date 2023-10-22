from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'cadastro', views.cadastro, name='cadastro'),
    url(r'delCadastro/(?P<cod>[0-9]+)/', views.delCadastro, name='delCadastro'),
    url(r'consultaCadastro/(?P<cod>[0-9]+)/', views.consultaCadastro, name='consultaCadastro'),
] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)