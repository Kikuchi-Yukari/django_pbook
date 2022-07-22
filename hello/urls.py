from django.urls import path
from . import views
from .views import PbookList

urlpatterns = [
    path('', views.index, name='index'),
    path('flower', views.flower, name='flower'),
    path('insect', views.insect, name='insect'),
    path('everything', views.everything, name='everything'),
    path('login', views.login, name='login'),
    path('account', views.account, name='account'),
    path('create', views.create, name='create'),    
    path('success', views.success, name='success'),
    path('upgrading', views.upgrading, name='upgrading'),
]

