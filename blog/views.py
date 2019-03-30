from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required


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