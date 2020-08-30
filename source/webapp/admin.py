from django.contrib import admin

from webapp.models import Poll, Choice, Answer


class ChoiceAdmin(admin.TabularInline):
    model = Choice
    extra = 0


class AnswerAdmin(admin.TabularInline):
    model = Answer
    fields = ('choice', 'created_at')
    readonly_fields = ('created_at',)
    extra = 0


class PollAdmin(admin.ModelAdmin):
    inlines = (ChoiceAdmin, AnswerAdmin)


admin.site.register(Poll, PollAdmin)
