from django.contrib import admin

from webapp.models import Poll, Choice


class ChoiceAdmin(admin.TabularInline):
    model = Choice


class PollAdmin(admin.ModelAdmin):
    inlines = (ChoiceAdmin,)


admin.site.register(Poll, PollAdmin)
