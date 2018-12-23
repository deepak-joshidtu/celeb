from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Login', views.login, name='login'),
    path('Signup', views.signup, name='signup'),
    path('Browse', views.browse, name='browse'),
    path('signsub', views.signsub, name='signsub'),
    path('userpage', views.userpage, name='userpage'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('supsub', views.supsub, name='supsub'),
    path('createrqst', views.createrqst, name='createrqst'),
    path('submitrqst', views.submitrqst, name='submitrqst'),
    path('celebprofile', views.celebprofile, name='celebprofile'),
    path('terms', views.terms, name='terms'),
     path('faq', views.faq, name='faq'),
    path('uploadv', views.uploadv, name='uploadv'),
]
