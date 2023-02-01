from django.shortcuts import render, HttpResponse
from rest_framework import generics, mixins, status
from .serializers import CarSerializer
from .models import Cars

def home(requests):
    return HttpResponse("<h1>Abhi</h1>")

class GenericView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    serializer_class = CarSerializer
    queryset = Cars.objects.all()
    lookup_field = 'id'    

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)