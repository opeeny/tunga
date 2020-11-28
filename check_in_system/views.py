from django.shortcuts import render
from .serializers import UserSerializer, VisitorSerializer
from rest_framework import permissions, renderers, viewsets
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
from .models import Visitor

# Create your views here.
class UserViewSet(viewsets.ReadOnlyModelViewSet):
#This viewset provides only List & Detail actions
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = (permissions.IsAuthenticated,)

class VisitorViewSet(viewsets.ModelViewSet):
    #This viewset automatically provides, list, create, retrieve, update & destroy actions
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer #Do other viewsets part from User & Group also have permissions
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)
    @action(detail = True, renderer_classes = [renderers.StaticHTMLRenderer])
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)