from django.contrib import admin
from .models import student_detail
from .models import teacher_detail
from .models import admin_detail

admin.site.register(student_detail)
admin.site.register(teacher_detail)
admin.site.register(admin_detail)