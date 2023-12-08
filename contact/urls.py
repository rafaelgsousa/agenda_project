from django.urls import path

from . import views

app_name = 'contact'

urlpatterns = [
    path('hello', views.hello, name='hello'),
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('contact/<uuid:contact_id>/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),
    
]
