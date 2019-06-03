from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import filters
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import TodoList
from .serializers import TodoListSerializers


# Create your views here.

class TodoPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class TodoListViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                      mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializers
    pagination_class = TodoPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('userid',)
    ordering_fields = ('time',)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
