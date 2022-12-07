from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
# from rest_framework import renderers
from rest_framework.renderers import BrowsableAPIRenderer,JSONRenderer

from .models import Setting, SettingGroup 
from .serializers import SettingSerializer, GroupSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class SettingListView(generics.ListCreateAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer

    # overwirte a method to modify how the instance
    # save is managed
    # perform_create is inherited from CreateModelMixin
    # by def. and used in create method
    def perform_create(self, serializer):
        # by def, ther is no logic to associate the user
        # that created the setting with the setting instance
        # we do this by using a proper. of the incoming request
        serializer.save(owner=self.request.user)
        
    # we can control permission
    # the global setting can be made in settings.py
    # , which can be overruled for each view
    # permisson_classes is ori.
    # APIView --> GenericAPIView --> ListCreateAPIView
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

class SettingDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Setting.objects.all()
    serializer_class = SettingSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

class GroupListView(generics.ListCreateAPIView):
    queryset = SettingGroup.objects.all()
    serializer_class = GroupSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SettingGroup.objects.all()
    serializer_class = GroupSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

# an endpoint for the root of AOI
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('applicationuser-list', request=request, format=format),
        'settings': reverse('setting-list', request=request, format=format),
        'settinggroups': reverse('settinggroup-list', request=request,format=format),
    })

class GroupHighlight(generics.GenericAPIView):
    queryset = SettingGroup.objects.all()
    renderer_classes = [BrowsableAPIRenderer,JSONRenderer]
    # serializer_class = GroupSerializer

    # def get(self, request, *arg, **kwargs):
    #     settinggroup = self.get_object()
    #     return Response(settinggroup.groupname)
