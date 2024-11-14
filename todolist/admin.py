from django.contrib import admin
from .models import Activity, Note, Modality
# Register your models here.


admin.site.register(Modality)
admin.site.register(Activity)
admin.site.register(Note)