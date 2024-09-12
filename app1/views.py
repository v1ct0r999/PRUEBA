from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola, esta es la vista de la app1, rama1.")