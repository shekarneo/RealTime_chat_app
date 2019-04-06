from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.

@login_required
def blog_post(request):
    if Post.objects.all().count() != 0:
        return render(request=request,
                  template_name='Post/post.html',
                  context={"Post":Post.objects.all()}
                  )
    else:
        return HttpResponse("<h4> No Post Available </h4>")

class PostListView(ListView):
    model = Post
    template_name = 'Post/post.html'
    context_object_name = 'Post'
    ordering = ['published_date']

class PostDetailView(DetailView):
    model = Post
    template_name = 'Post/post_detail.html'

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = 'blog'

    def test_func(self):
        blog_post = self.object()
        if self.request.user ==  blog_post.auther:
            return True
        return False