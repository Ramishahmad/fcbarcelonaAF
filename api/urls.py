from django.urls import path
from django.views.generic.base import TemplateView

from api.views import posts_serializer


app_name = 'api'

urlpatterns = [
    # Url of Main Page
    path('',posts_serializer),
    path('index/',TemplateView.as_view(template_name='api/index.html')),
]