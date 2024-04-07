from django.contrib import admin
from .models import Invitee, MessageToBride, Activity, ActivityResponse, Love

class InviteeAdmin(admin.ModelAdmin):
    readonly_fields = ('code',)
    list_display = ['name', 'code', 'quota', 'is_attended', 'display_invitation_url']
    list_per_page = 300

    def display_invitation_url(self, obj):
        return obj.invitation_url
    display_invitation_url.short_description = 'Invitation URL'

class ActivityAdmin(admin.ModelAdmin):
    pass

class ActivityResponseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Invitee, InviteeAdmin)
admin.site.register(MessageToBride)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(ActivityResponse, ActivityResponseAdmin)
admin.site.register(Love)