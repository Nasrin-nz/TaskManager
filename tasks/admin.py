from django.contrib import admin
from .models import Mission, Project, Task, Action, Referral

admin.site.register(Mission)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Action)
admin.site.register(Referral)
