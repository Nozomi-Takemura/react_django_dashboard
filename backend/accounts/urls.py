from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .models import ApplicationUser
from .views import ApplicationUserViewSet,ApplicationUserDetail,ApplicationUserList,\
ApplicationUserDetailAPIView,ApplicationUserListClassView,ApplicationUserDetailClassView,\
    ApplicationUserDetailMixinsView, ApplicationUserListMixinsView,\
    ApplicationUserListGenView, ApplicationUserDetailGenView

# define a map bet. url and its action
# router = routers.DefaultRouter()
# router.register(r'ApplicationUser', ApplicationUserViewSet)
# router.register(r'ApplicationUser/<int:pk>/', ApplicationUserDetail)

urlpatterns = [
    # path('', include(router.urls)),
    path('ApplicationUser/', ApplicationUserList),
    path('ApplicationUser/<uuid:pk>/', ApplicationUserDetailAPIView),
    path('ApplicationUser/Class/', ApplicationUserListClassView.as_view()),
    path('ApplicationUser/Class/<uuid:pk>/', ApplicationUserDetailClassView.as_view()),    
    path('ApplicationUser/Mixins/', ApplicationUserListMixinsView.as_view()),
    path('ApplicationUser/Mixins/<uuid:pk>/', ApplicationUserDetailMixinsView.as_view()),    
    path('ApplicationUser/Gen/', ApplicationUserListGenView.as_view(),name='applicationuser-list'),
    path('ApplicationUser/Gen/<uuid:pk>/', ApplicationUserDetailGenView.as_view(),name='applicationuser-detail'),    
]

urlpatterns = format_suffix_patterns(urlpatterns)