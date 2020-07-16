from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('postjob/', views.simpleform, name = "simpleform"),
    path('postjob/thanks/', views.thanks, name = "thanks"),
    path('postjob/jobs/', views.jobs_display, name = "job_display"),
    path('search/', views.search, name = "search"),
]