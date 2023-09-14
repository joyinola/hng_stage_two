from django.shortcuts import render
from person_db.serializers import PersonSerializer
from rest_framework import generics
from rest_framework.response import Response
from .models import Person
from rest_framework.mixins import RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,CreateModelMixin
# Create your views here.

class CreatePerson(generics.GenericAPIView,CreateModelMixin):

    serializer_class=PersonSerializer
    def post(self,reqest,*args,**kwargs):
        return self.create(reqest,*args,**kwargs)

class OtherOperation(generics.GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    serializer_class=PersonSerializer
    queryset=Person.objects.all()
    lookup_field= 'id'
    
    def get(self,reqest,*args,**kwargs):
        return self.retrieve(reqest,*args,**kwargs)
    
    def patch(self,reqest,*args,**kwargs):
        return self.partial_update(reqest,*args,**kwargs)
    
    
    def delete(self,reqest,*args,**kwargs):
        delete_op=self.destroy(reqest,*args,**kwargs)
        return Response({'message':'Sucessfully Deleted'})