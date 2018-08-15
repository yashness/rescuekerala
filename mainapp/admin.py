from django.contrib import admin
from .models import Request, Volunteer, Contributor, DistrictNeed, DistrictCollection, DistrictManager


class RequestAdmin(admin.ModelAdmin):
    readonly_fields = ('dateadded',)
    ordering = ('district',)
    list_filter = ('district', 'status',)


class VolunteerAdmin(admin.ModelAdmin):
    readonly_fields = ('joined',)
    list_display = ('name', 'phone', 'organisation', 'joined')
    list_filter = ('district', 'joined',)

class ContributorAdmin(admin.ModelAdmin):
    list_filter = ('district', 'status',)

admin.site.register(Request, RequestAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(DistrictNeed)
admin.site.register(DistrictCollection)
admin.site.register(DistrictManager)
