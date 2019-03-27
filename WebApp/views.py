from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse


#create your views here
def index(request):
    return render(request, 'webapp/home.html')

def contact(request):
    return render(request, 'webapp/basic.html', {'content': ['contact #########']})


def log_out(request):

    return render(request, 'registration/log_out.html')