from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404

from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'queryset'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        latest_list = Post.objects.order_by('-timestamp')
        context = super().get_context_data(**kwargs)
        context['latest'] = latest_list
        context['page_request_var'] = "page"
        context['title'] = 'Blog'
        return context

    def get_queryset(self):
        return Post.objects.order_by('-timestamp')

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
    'post': post,
    'title' : 'Post'
    }
    return render(request, 'post.html', context)