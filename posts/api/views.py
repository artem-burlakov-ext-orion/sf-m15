from rest_framework import generics
from posts.models import Post, Category
from posts.api.serializers import PostSerializer, PostSerializerOneCategory

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostListViewOneCategory(generics.ListAPIView):
    model = Post
    serializer_class = PostSerializerOneCategory

    def get_queryset(self):
        slug = self.kwargs['slug']
        queryset = Post.objects.filter(category__slug=slug)
        return queryset
