from django.urls import path
from .views import CreatePerson,OtherOperation

urlpatterns= [
    path('', CreatePerson.as_view(),name='create'),
    path('<int:id>/',OtherOperation.as_view(),name='operations')
    
]