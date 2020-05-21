from django.contrib import admin
from .models import *

# Register your models here.


class ProjectInline(admin.TabularInline):
    model = Projects
    extra = 0


class TechUseInLine(admin.TabularInline):
    model = TechUsed
    extra = 0


class TaskInLine(admin.TabularInline):
    model = Task
    extra = 0


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [('project_name', 'link'), ('school', 'job')]
        }),
        (' ', {
            'fields': ['description']
        })
    ]
    inlines = [TechUseInLine, TaskInLine]
    list_display = ["project_name", "link", "school", "job"]


class JobAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [('position', 'work_name'), 'link', 'extra']
        }),
        ('Location', {
            'fields': ['city', 'state', 'country']
        }),
        ('Dates', {
            'fields': [('from_month', 'from_year'), 'current_job', ('end_month', 'end_year')]
        }),
        (' ', {
            'fields': ['description']
        })
    ]
    inlines = [ProjectInline, TaskInLine]
    list_display = ["position", "work_name", "extra", "current_job"]


class SchoolAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [('degree', 'major'), 'school']
        }),
        ('Location', {
            'fields': ['city', 'state', 'country']
        }),
        ('Dates', {
            'fields': [('from_month', 'from_year'), 'current_school', ('end_month', 'end_year')]
        }),
    ]
    inlines = [ProjectInline, TaskInLine]
    list_display = ["schoolid", "degree", "major", "school", 'current_school']


class TechAdmin(admin.ModelAdmin):
    list_display = ["technology", "category", "proficiency", "years"]


class TechUseAdmin(admin.ModelAdmin):
    list_display = ['project', 'technology']


class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "project", "work", "school"]


admin.site.register(profile)
admin.site.register(Technology, TechAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(WorkPlaces, JobAdmin)
admin.site.register(Projects, ProjectAdmin)
admin.site.register(TechUsed, TechUseAdmin)
admin.site.register(Task)
