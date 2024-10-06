from django.contrib import admin

# Register your models here.
from .models import Employee,Student
# @admin.register(Employee)
class shoolAdmin(admin.ModelAdmin):
    admin.site.site_header = 'School Management System'
    admin.site.register(Employee)
    admin.site.register(Student)
    
# @admin.register(Employee)
# class Staff_Admin(admin.ModelAdmin):
#     admin.site.site_header = 'School Management System'
#     list_display=("id","name","fname","designation","scale")

# @admin.register(Student)
# class Staff_Admin(admin.ModelAdmin):
#     admin.site.site_header = 'School Management System'
#     list_display=("id","admission_no","name","fathername","class_enrolled")
