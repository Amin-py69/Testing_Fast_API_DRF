from django.urls import path
from . import views

urlpatterns = [
    path('', views.TestApi.as_view()),
    path('pro', views.ProductApi.as_view()),
    path('detail/<int:pk>', views.ProductDitailApi.as_view()),
    path('detail/add', views.ProductAddApi.as_view()),
    path('detail/update/<int:pk>', views.ProductUpdateApi.as_view()),
    path('detail/delete/<int:pk>', views.ProductDeleteApi.as_view()),
    # path('coin', views.GetCryptoPrice.as_view()),
]