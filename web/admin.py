from django.contrib import admin

from web.models import CsvFiles


class CsvFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'file', 'date_added')

admin.site.register(CsvFiles)
