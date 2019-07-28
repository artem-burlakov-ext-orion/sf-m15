from django.shortcuts import render
from .models import Post, Category
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse



# Create your views here.


class PostsListView(ListView):
    queryset = Post.objects.filter(status='published')
    context_object_name = 'posts'
    template = 'posts/post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class PostsListOneCategoryView(ListView):

    context_object_name = 'posts'
    template = 'posts/post_list.html'

    def get_queryset(self,**kwargs):
        cat = self.kwargs['cat']
        return Post.objects.filter(category=cat)


# def about_api(request):
#
#     return render(request,'posts/api.html')

class AboutApiListView(ListView):
    queryset = Category.objects.all()
    context_object_name = 'categories'
    template_name = 'posts/api.html'



def json_list_published_posts(request):
    posts = Post.objects.filter(status='published')

    return JsonResponse(
        {
            'posts': [
                {'title': p.title,
                 'slug': p.slug,
                 'id': p.id,
                 'published': p.when_published,
                }
                for p in posts
                ]
        }
        )
