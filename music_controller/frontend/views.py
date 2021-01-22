from django.shortcuts import render

# Create your views here.
def index(request, *args, **kwargs):
# def index(request):
    return render(request, 'frontend/index.html')