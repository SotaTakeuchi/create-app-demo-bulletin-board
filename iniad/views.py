from django.shortcuts import render
from django.views import generic


# Create your views here.

class IndexViews(generic.TemplateView):
    template_name='index.html'

class ScheduleViews(generic.TemplateView):
    template_name='schedule.html'

class VideosViews(generic.TemplateView):
    template_name='videos.html'