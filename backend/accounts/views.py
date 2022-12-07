from django.shortcuts import render
from rest_framework import viewsets, status
from django.contrib.auth import get_user_model
from .serializers import ApplicationUserSerializer
# delete later ...
from django.http import HttpResponse, JsonResponse, Http404
# from rest_framework.response import 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# mixin
from rest_framework import mixins
from rest_framework import generics

#

# Create your views here.

# ViewSets define the (api)view behavior
class ApplicationUserViewSet(viewsets.ModelViewSet):
    user = get_user_model()
    queryset = user.objects.all()
    serializer_class = ApplicationUserSerializer

class ApplicationUserListClassView(APIView):
    def get(self, request, format=None):
        users = get_user_model().objects.all()
        serializer = ApplicationUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ApplicationUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ApplicationUserDetailClassView(APIView):
    def get_object(self, pk):
        try:
            return get_user_model().objects.get(pk=pk)
        except get_user_model().DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = ApplicationUserSerializer(user)
        return Response()

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = ApplicationUserSerializer()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQEST)
    
    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_400_BAD_REQUEST)

# mixins
class ApplicationUserListMixinsView(mixins.ListModelMixin,\
    mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = ApplicationUserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class ApplicationUserDetailMixinsView(mixins.RetrieveModelMixin,\
    mixins.UpdateModelMixin, mixins.DestroyModelMixin,\
        generics.GenericAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = ApplicationUserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# generic REST framework
class ApplicationUserListGenView(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = ApplicationUserSerializer
class ApplicationUserDetailGenView(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = ApplicationUserSerializer
            


@api_view(['GET', 'POST'])
def ApplicationUserList(request, format=None):
    """
    List all users, or create new user
    """
    if request.method == 'GET':
        users = get_user_model().objects.all()
        serializer = ApplicationUserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ApplicationUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def ApplicationUserDetail(request, pk):
    """
    Retrieve, update, or delete user
    """
    try:
        USER = get_user_model()
        user = user.objects.get(pk=pk)
    except user.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        data = JSONParser().parse(request)
        serializer = ApplicationUserSerializer(get_user_model(), data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ApplicationUserSerializer(get_user_model(), data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        get_user_model().delete()
        return HttpResponse(status=204)

@api_view(['GET', 'PUT', 'DELETE'])
def ApplicationUserDetailAPIView(request, pk, format=None):
    """
    Retrieve, update, or delete user
    """
    try:
        USER = get_user_model()
        user = USER.objects.get(pk=pk)
    except user.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ApplicationUserSerializer(get_user_model(), data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        serializer = ApplicationUserSerializer(get_user_model(), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        get_user_model().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
