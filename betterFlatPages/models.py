from django.db import models
from django.urls import reverse, NoReverseMatch, get_script_prefix
from django.utils.encoding import iri_to_uri
from django.utils.translation import gettext_lazy as _
from django.contrib.sites.models import Site
# Create your models here.
class FlatPage(models.Model):
    url = models.CharField(_('URL'), max_length=100, db_index=True)
    title = models.CharField(_('title'), max_length=200)
    content = models.TextField(_('content'), blank=True)
    enable_comments = models.BooleanField(_('enable comments'), default=False)
    meta = models.TextField(blank=True,help_text=_(
            'Example: <code>&#60;meta name="viewport" content="width=device-width, initial-scale=1"&#62;'
            '<br/>&#60;meta name="something else" content="something else goes here"&#62;</code>.'
        ),)
    template_name = models.CharField(
        _('template name'),
        max_length=70,
        blank=True,
        help_text=_(
            'Example: “betterFlatPages/contact_page.html”. If this isn’t provided, '
            'the system will use “betterFlatPages/default.html”.'
        ),
    )
    registration_required = models.BooleanField(
        _('registration required'),
        help_text=_("If this is checked, only logged-in users will be able to view the page."),
        default=False,
    )
    sites = models.ManyToManyField(Site, verbose_name=_('sites'))

    class Meta:
        verbose_name = _('flat page')
        verbose_name_plural = _('flat pages')
        ordering = ['url']

    def __str__(self):
        return "%s -- %s" % (self.url, self.title)

    def get_absolute_url(self):
        from .views import flatPageView

        for url in (self.url.lstrip('/'), self.url):
            try:
                return reverse('betterFlatPages:pages', kwargs={'url': url})
            except NoReverseMatch:
                pass
        # Handle script prefix manually because we bypass reverse()
        return iri_to_uri(get_script_prefix().rstrip('/') + self.url)
