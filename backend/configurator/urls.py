from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from .models import Setting
from .views import SettingListView, SettingDetailView, api_root, GroupHighlight, GroupListView, GroupDetailView

urlpatterns = [
    path('', api_root),
    path('setting/', SettingListView.as_view(),name='setting-list'),
    path('setting/<uuid:pk>/', SettingDetailView.as_view(), name='setting-detail'),
    path('setting/<uuid:pk>/grouphighlight/',GroupHighlight.as_view(),name='group-highlight'),
    path('settinggroup/', GroupListView.as_view(),name='settinggroup-list'),
    path('settinggroup/<uuid:pk>/', GroupDetailView.as_view(), name='settinggroup-detail'),
    # path('group/<uuid:pk>//',GroupHighlight.as_view(),name='group-highlight')
]

urlpatterns = format_suffix_patterns(urlpatterns)