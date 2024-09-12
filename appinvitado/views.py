from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola, mundo. Esta es la página de inicio de la app  invitado")
