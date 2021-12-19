from django.contrib import admin
from .models import FlatPage
from .forms import FlatpageForm
from django.utils.translation import gettext_lazy as _
# Register your models here.
@admin.register(FlatPage)
class FlatPageAdmin(admin.ModelAdmin):
    form = FlatpageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': ('registration_required','enable_comments', 'template_name','meta'),
        }),
    )
    list_display = ('url', 'title')
    list_filter = ('sites', 'registration_required')
    search_fields = ('url', 'title')
