from django.shortcuts import render, HttpResponse


# контроллер
# Create your views here.
def index(request):
    return render(request, 'home/index.html')
