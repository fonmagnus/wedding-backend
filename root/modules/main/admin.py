from django.contrib import admin
from .models import Invitee, MessageToBride, Activity, ActivityResponse

class InviteeAdmin(admin.ModelAdmin):
    readonly_fields = ('code',)
    list_display = ['name', 'code', 'quota', 'is_attended']
    list_per_page = 300

class ActivityAdmin(admin.ModelAdmin):
    pass

class ActivityResponseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Invitee, InviteeAdmin)
admin.site.register(MessageToBride)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(ActivityResponse, ActivityResponseAdmin)
