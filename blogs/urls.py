from django.urls import path
from . import views
from rest_framework.authtoken import views as token_views

urlpatterns = [
    path('show', views.BlogShowView.as_view()),
    path('details/<int:pk>', views.BlogDetailView.as_view()),
    path('adds', views.BlogAddView.as_view()),
    path('updated/<int:pk>', views.BlogUpdateView.as_view()),
    path('deleted/<int:pk>', views.BlogDeleteView.as_view()),
    path('deleted/<int:pk>', views.BlogDeleteView.as_view()),
    path('tokens', views.CheckToken.as_view()),
    path('login', token_views.obtain_auth_token),
    path('comment', views.ShowCommentView.as_view()),
]
