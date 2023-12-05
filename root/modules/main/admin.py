from django.contrib import admin
from .models import Invitee, MessageToBride

class InviteeAdmin(admin.ModelAdmin):
    readonly_fields = ('code',)
    list_display = ['name', 'code', 'quota', 'is_attended']
    list_per_page = 300

admin.site.register(Invitee, InviteeAdmin)
admin.site.register(MessageToBride)