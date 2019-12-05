from django.contrib import admin
from .models import MeetingRoom, RoomAgenda

class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_no', 'info')

class RoomAgendaAdmin(admin.ModelAdmin):
    list_display = ('room', 'date')

admin.site.register(MeetingRoom, RoomAdmin)
admin.site.register(RoomAgenda, RoomAgendaAdmin)
