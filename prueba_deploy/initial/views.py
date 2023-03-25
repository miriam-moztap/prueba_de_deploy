#from django.http import HttpResponse

#def index(request):
    #return HttpResponse('Hola!! vamos por ese deploy!')
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloDrf(APIView):
    def get (self, request, format=None):
        return Response({"message": 'YA CASI QUEDA!'})


