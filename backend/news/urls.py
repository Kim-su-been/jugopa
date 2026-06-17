from django.urls import path

from . import views

app_name = 'news'

urlpatterns = [
	path('sectors/today/', views.sectors_today, name='sectors_today'),
]
