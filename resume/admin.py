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


class ProjectImagesInline(admin.StackedInline):
    model = ProjectImages
    extra = 0


class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['profile_pic',
                       ('first_name', 'last_name', 'occupation'),
                       ('location_city', 'location_state'),
                       ]
        }),
        ('Contact', {
            'fields': [
                ('email', 'email2'),
                ('linkedin', 'bitbucket', 'github'),
            ]
        }),
        ('Bio', {
            'fields': ['bio', 'interest', 'pro_bio']
        })
    ]


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['project_image',
                       ('project_name', 'link'),
                       ('school', 'job', 'personal')]
        }),
        ('Dates', {
            'fields': [
                ('from_month', 'from_year'),
                'in_progress',
                ('end_month', 'end_year'),
            ]
        }),
        (' ', {
            'fields': ['role', 'description']
        }),

    ]
    inlines = [ProjectImagesInline, TechUseInLine, TaskInLine]
    list_display = ["project_name", "link", "project_image", "role"]


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
    inlines = [ProjectInline]
    list_display = ["position", "work_name", "extra", "current_job"]


class SchoolAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [('degree', 'concentration'), 'school']
        }),
        ('Location', {
            'fields': ['city', 'state', 'country']
        }),
        ('Dates', {
            'fields': [('from_month', 'from_year'), 'current_school', ('end_month', 'end_year')]
        }),
    ]
    inlines = [ProjectInline]
    list_display = ["id", "degree", "concentration", "school", 'current_school']


class TechAdmin(admin.ModelAdmin):
    list_display = ["technology", "category", "proficiency", "years"]


class TechUseAdmin(admin.ModelAdmin):
    list_display = ['project', 'technology']


class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "project"]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Technology, TechAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(WorkPlaces, JobAdmin)
admin.site.register(Projects, ProjectAdmin)
admin.site.register(TechUsed, TechUseAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Certification)
admin.site.register(ProjectImages)

# admin.site.register(Profile)
# admin.site.register(Technology)
# admin.site.register(Task)
# admin.site.register(WorkPlaces)
# admin.site.register(School)
# admin.site.register(ProjectType)
# admin.site.register(TechUsed)
# admin.site.register()
