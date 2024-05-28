from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'main/index.html', context={'text':'hi there!'})

def test(request):
    return render(request, 'main/test.html', context={'first_name':'Sruli','last_name':'Baum'})