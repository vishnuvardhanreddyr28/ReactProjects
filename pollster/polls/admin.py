from django.contrib import admin
from .models import pollQuestion,Choice


admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Web Pollster Admin"



# Register your models here.

admin.site.register(pollQuestion)
admin.site.register(Choice)
