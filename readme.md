# django-betterFlatPages

This django app is a drop in replacement for django.contrib.flatpages. The main new features that django-betterFlatPages offers as of now is the optional django-rest-framework views and a spot to add metadata. Any contribution is welcome just make a pull request, and I will try to add your feature in the next version as soon as possible.

## Installation
1. prerequisites
   * sites framework (django.contrib.sites) - make sure you have the site id set
   * django-rest-framework (not required unless you want to use betterFlatPages rest api)
2. run `pip install django-betterFlatPages`
3. Add 'betterFlatPages' to your INSTALLED_APPS setting.
4. Add urls (only add the urls file that you plan on using)
    

    #rest api urls
    urlpatterns = [
        path('api/pages/', include('betterFlatPages.DRF_urls')),
    ]

    #normal urls file
    urlpatterns = [
        path('pages/', include('betterFlatPages.urls')),
    ]
5. Run the command `manage.py migrate`.

## using the rest api
> to use the rest api django-rest-framework must be installed

to get the page in the rest api add the url at the end of `api/pages/`

if the flatPage url is `/policy/` then it would be `/api/pages/policy/'

the response would look something like

    {
        "url": "/policy/",
        "title": "privacy policy",
        "content": "this is the privacy policy",
        "enable_comments": false,
        "meta": "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
    }

## using custom templates

By default, flatpages are rendered via the template `betterFlatPages/default.html`, but you can override that for a particular flatpage: in the admin, a collapsed fieldset titled “Advanced options” (clicking will expand it) contains a field for specifying a template name. If you’re creating a flat page via the Python API you can set the template name as the field template_name on the FlatPage object. (as per the django documentation)

Flatpage templates are passed a single context variable, flatpage, which is the flatpage object.

here is the current `default.html`

    {% extends 'betterFlatPages/base.html' %}
    {% block head_title %}{{ flatpage.title }}{% endblock %}
    
    {% block extra_head %}{{ flatpage.meta | safe}}{% endblock %}
    
    {% block content %}
    <div class="bg-white p-5 rounded">
        <h1 class="text-center">{{ flatpage.title }}</h1>
        {{ flatpage.content | safe }}
    </div>
    {% endblock %}

## using metatags

you can add meta-tags in the admin in “Advanced options" dropdown

add the meta options with the full tag just like it would be in html

    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="product" content="cool product">
    <meta name="etc" content="etc...">

to render the tags on your template page add

    <head>
        ...
        {{ flatpage.meta | safe}}
        ...
    </head>

### extending and overriding the template
visit: https://docs.djangoproject.com/en/4.0/howto/overriding-templates/

## still left to do 
* create a management command to copy all the django.contrib.flatpages pages to better flat pages (and possibly the reverse)
* amazing documentation
* 100% testing coverage
* create a replacement middleware similar to django.contrib.flatpages.middleware.FlatpageFallbackMiddleware
* add any new features django.contrib.flatpages is lacking
* add all the features that django.contrib.flatpages has
  * template tags
  * integration with django sitemaps
  * use marksafe before rendering template so user doesn't have to use the | safe filter

