from django.contrib import admin
from anshaj import models
# Register your models here.
admin.site.register(models.job_post)
admin.site.register(models.applyed_candidates)
admin.site.register(models.job_category)
admin.site.register(models.Interview_attended_datas)
admin.site.register(models.Shortlisted)