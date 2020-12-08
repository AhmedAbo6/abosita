from django.urls import path
from . import views as core_views

urlpatterns  =  [
    path('test/', core_views.home, name='Home'),
    path('', core_views.about, name='About'),
    path('contact/', core_views.contact, name='Contact'),
    path('post/', core_views.post),
    path('blog/', core_views.blog),

]