from django.shortcuts import render
from django.template import Context
from django.views.generic import DetailView

from api.models import Post


def list(request):
    return render(request, 'main/index.html')


def detail(request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        'id': post.id
    }
    return render(request, 'main/detail.html', context)


class PostDetailView(DetailView):
    model = Post
    template_name = 'main/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["post_item"] = Post.objects.get(slug=self.kwargs["slug"])
        return context
