from django.contrib import admin
from .models import Note, Profile, TODO, Note, StudyMaterials
# Register your models here.

admin.site.register(Profile)
admin.site.register(TODO)
admin.site.register(Note)
admin.site.register(StudyMaterials)