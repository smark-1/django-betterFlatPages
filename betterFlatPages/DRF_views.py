from django.contrib.sites.shortcuts import get_current_site
from rest_framework.generics import get_object_or_404
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN
from rest_framework.views import APIView

from betterFlatPages.models import FlatPage

class flatPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlatPage

        exclude = ['sites','registration_required','template_name','id']


class flatPageAPIView(APIView):
    serializer_class = flatPageSerializer

    # override default permissions
    permission_classes = []

    def get_object(self):
        # get the flat page object
        url = "/" + self.kwargs['url']

        site_id = get_current_site(self.request).id
        return get_object_or_404(FlatPage, url=url, sites=site_id)

    def get(self,request,url):
        flatPage = self.get_object()

        if flatPage.registration_required and not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."},status=HTTP_403_FORBIDDEN)

        else:
            return Response(self.serializer_class(flatPage).data)