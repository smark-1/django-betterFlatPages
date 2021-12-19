from django.urls import path, include
from .views import flatPageView

app_name = 'betterFlatPages'

urlpatterns = [
    path("<path:url>", flatPageView, name='pages'),
]