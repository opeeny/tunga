from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Visitor


class UserSerializer(serializers.HyperlinkedModelSerializer):
    visitor = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = User
        fields = ['url', 'visitor', 'username', 'email', 'groups']


class VisitorSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Visitor
        fields  = ['url', 'owner', 'name', 'id_number', 'telephone_number', 'temperature', 'company', 'date']