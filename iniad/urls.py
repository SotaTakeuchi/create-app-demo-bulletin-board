from django.urls import path

from . import views

app_name='iniad'
urlpatterns = [
    path('', views.IndexViews.as_view() , name='index'),
    path('schedule/', views.ScheduleViews.as_view(), name='schedule'),
#    path('<str:room_name>/', views.room, name='room'),
]
#added
