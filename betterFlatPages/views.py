from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from .models import FlatPage
from django.contrib.auth.views import redirect_to_login
from django.template import loader
import os

DEFAULT_TEMPLATE = os.path.join('betterFlatPages','default.html')

# Create your views here.
def flatPageView(request,url):
    # get the flat page object
    if not url.startswith("/"):
        url="/"+url
    site_id = get_current_site(request).id
    flatPage = get_object_or_404(FlatPage,url=url,sites=site_id)

    if flatPage.registration_required and not request.user.is_authenticated:
        return redirect_to_login(request.path)

    # get the flat page template
    if flatPage.template_name:
        template = loader.select_template((flatPage.template_name, DEFAULT_TEMPLATE))
    else:
        template = loader.get_template(DEFAULT_TEMPLATE)

    return HttpResponse(template.render({'flatpage': flatPage}, request))
