from django.contrib import admin
from cinema.models import *


class CinemaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class SoonAdmin(admin.ModelAdmin):
    prepopulated_fields = {"cinema_slug": ("title",)}


admin.site.register(Cinema, CinemaAdmin)
admin.site.register(Soon, SoonAdmin)
admin.site.register(Theatr)
admin.site.register(TSeans)
admin.site.register(Seat)
admin.site.register(Ticket)
admin.site.register(Seans)

