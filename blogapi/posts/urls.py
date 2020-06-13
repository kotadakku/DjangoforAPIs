from django.urls import path
from rest_framework.routers import SimpleRouter


from . import views

urlpatterns = [
    path('<int:pk>', views.PostDetail.as_view(), name ='detail'),
    path('', views.PostList.as_view(), name ='list'),
    path('users/', views.UserList.as_view()), # new
    path('users/<int:pk>/', views.UserDetail.as_view()),

]

# router = SimpleRouter()
# router.register('users', views.UserViewSet, base_name='users')
# router.register('', views.PostViewSet, base_name='posts')
# urlpatterns = router.urls
