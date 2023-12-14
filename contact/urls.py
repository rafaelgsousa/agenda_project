from django.urls import path

from . import views

app_name = 'contact'

urlpatterns = [
    path('hello', views.hello, name='hello'),
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    #Contact CRUD
    path('contact/<uuid:contact_id>/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),
    path('contact/<uuid:contact_id>/update/', views.update, name='update'),
    path('contact/<uuid:contact_id>/delete/', views.delete, name='delete'),
    # user
    path('user/create/', views.register, name='register'),
]
