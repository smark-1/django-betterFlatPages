from django.urls import path
from .DRF_views import flatPageAPIView
app_name = 'betterFlatPages_api'

urlpatterns = [
    path("<path:url>", flatPageAPIView.as_view(), name='pages')
]