from flat_pages.models import FlatPage
from django.contrib import admin

class FlatPageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(FlatPage, FlatPageAdmin)
