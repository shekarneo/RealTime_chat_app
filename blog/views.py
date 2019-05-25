from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import AddPostForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.

@login_required()
def add_post(request):
    form = AddPostForm(request.POST or None)
    if request.method == "POST":

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
        return redirect(blog_post)

    return render(request=request,
                   template_name='Post/post_add.html',
                  context={'form': form},
                  )


@login_required
def blog_post(request):
    usr = request.user
    form = AddPostForm(request.POST or None)
    if Post.objects.filter(author__username=usr).count() != 0:
    #if Post.objects.all().count() != 0:
        # return HttpResponse("<p> usr </p>")
        return render(request=request,
                      template_name='Post/post.html',
                      context={"Post": Post.objects.filter(author__username=usr)}
                      )
    else:
        return redirect(add_post)

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


