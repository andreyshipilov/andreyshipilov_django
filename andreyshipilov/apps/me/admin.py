from django.contrib import admin

from models import Social, Project, ProjectType, Participant, Participation, \
                   Screenshot, Role, Tweet
from hvad.admin import TranslatableAdmin


admin.site.register(Social)


# Participations
class ParticipantAdmin(TranslatableAdmin):
    pass
admin.site.register(Participant, ParticipantAdmin)

class RoleAdmin(TranslatableAdmin):
    pass
admin.site.register(Role, RoleAdmin)


# Projects
class ParticipationInline(admin.TabularInline):
    extra = 1
    model = Participation

class ScreenshotInline(admin.TabularInline):
    extra = 1
    model = Screenshot

class ProjectAdmin(TranslatableAdmin):
    list_display = ('__unicode__', 'date', 'is_alive', 'is_published')
    list_filter = ('project_type',)
    inlines = (ParticipationInline, ScreenshotInline)
admin.site.register(Project, ProjectAdmin)

class ProjectTypeAdmin(TranslatableAdmin):
    pass
admin.site.register(ProjectType, ProjectTypeAdmin)


class TweetAdmin(admin.ModelAdmin):
    list_display = ('text', 'country', 'date', 'latitude', 'longitude',)
    list_filter = ('country',)
admin.site.register(Tweet, TweetAdmin)
