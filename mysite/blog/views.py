from django.views.generic import ListView, DetailView
from blog.models.post import Post


class PostView(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'post-detail.html'

# Create your views here.
