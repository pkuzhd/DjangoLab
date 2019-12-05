from django.contrib import admin
from .models import Items, History

class ItemsAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'serial', 'position')

class HistoryAdmin(admin.ModelAdmin):
    list_display = ('date', 'item', 'user', 'back')

admin.site.register(Items, ItemsAdmin)
admin.site.register(History, HistoryAdmin)
