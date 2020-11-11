from django.conf.urls import url, include
from rest_framework import routers
from api.views import UserViewSet


from rest_framework_simplejwt import views as jwt_views 
from . import views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^upload/$', views.MyFileView.as_view(), name='file-upload'),


    url(r'^token/', 
         jwt_views.TokenObtainPairView.as_view(), 
         name ='token_obtain_pair'), 
    url(r'^token/refresh/', 
         jwt_views.TokenRefreshView.as_view(), 
         name ='token_refresh'), 

] 

