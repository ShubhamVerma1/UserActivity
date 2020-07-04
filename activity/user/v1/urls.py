"""Endpoints of APIs for user."""

from django.urls import path

from user.v1 import views

app_name = 'user'

urlpatterns = [
    path('all_user_activities', views.UserActivityView.as_view(),
         name='all_user_activites')
]
