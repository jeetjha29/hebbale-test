from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import CategoryView
from rest_framework.response import Response
from rest_framework import generics, status, serializers
from rest_framework.pagination import PageNumberPagination
from myapp.serializers import ListCatSerializer, AddCatSerializer

def hello(request):     
    return HttpResponse("Hello, world!")

class ListCatView(generics.ListAPIView):
    serializer_class = ListCatSerializer
    queryset = CategoryView.objects.all()
    print(queryset)
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        response = JsonResponse(serializer.data)
        response["Access-Control-Allow-Origin"] = "*"
        return response


class AddCatView(generics.CreateAPIView):
    serializer_class = AddCatSerializer

    def create(self, request, *args, **kwargs):
        cat_serializer = self.get_serializer(data=request.data)
        cat_serializer.is_valid(raise_exception=True)
        cat_serializer.save()
        return Response(cat_serializer.data, status=status.HTTP_201_CREATED)
