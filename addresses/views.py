from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import AddressSerializer
from .models import Addresses
# Create your views here.

@csrf_exempt
def address_list(request):

    if request.method == 'GET':
        queryset = Addresses.objects.all()
        serializer = AddressSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AddressSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def address(request, pk):

    obj = Addresses.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = AddressSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AddressSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)


@csrf_exempt
def login(request):

    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_name = data['name']
        obj = Addresses.objects.get(name=search_name)
        print(obj.phone_number)

        if data['phone_number'] == obj.phone_number:
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)
