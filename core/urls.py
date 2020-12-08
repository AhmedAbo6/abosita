from django.urls import path
from . import views as core_views
from posts import views as posts_views

urlpatterns  =  [
    path('test/', core_views.home, name='Home'),
    path('', core_views.about, name='About'),
    path('contact/', core_views.contact, name='Contact'),
    path('blog/', posts_views.PostListView.as_view(), name='Blog'),
    path('post/<slug:slug>/', posts_views.post, name='Post'),


]