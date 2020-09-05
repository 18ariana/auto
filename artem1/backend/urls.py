from django.urls import path
from . import views

order_detail = views.OrderViewset.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('orders/', views.OrderListView.as_view()),
    path('order/<int:pk>/', order_detail),
    path('add_order', views.OrderAddView.as_view()),
    path('order/update/<int:pk>/', views.OrderPartialUpdateView.as_view()),
    path('order_detail/<int:pk>/', views.OrderDetailView.as_view()),
    path('logout/', views.Logout.as_view()),
    path('status/', views.StatusView.as_view())]
