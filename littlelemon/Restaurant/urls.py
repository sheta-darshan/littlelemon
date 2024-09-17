from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu-item'),
    path('restaurant/booking', include(router.urls)),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
]
