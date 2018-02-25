# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import User, Project, project_user, user_commit

admin.site.register(User)
admin.site.register(Project)
admin.site.register(project_user)
admin.site.register(user_commit)

# Register your models here.
