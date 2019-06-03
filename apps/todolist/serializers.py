from rest_framework import serializers
from django.db.models import Q
from .models import TodoList


class TodoListSerializers(serializers.ModelSerializer):

    class Meta:
        model = TodoList
        fields = "__all__"