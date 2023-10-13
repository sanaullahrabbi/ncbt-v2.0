from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User,Group
from django.utils.translation import gettext as _
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Department)


admin.site.site_header = 'NCBT ADMIN PORTAL'


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_staff',
                'is_active')
    fieldsets = (
        (("User Details"), {'fields': ('username','email', 'password')}),
        (_("Account Details"), {'fields': ('date_joined', 'last_login')}),
        (_("Permission"), {'fields': ('is_active', 'is_staff',)}),
    )
    add_fieldsets = (
        ("User Details", {'fields': ('username','email', 'password1', 'password2')}),
        ("Permission", {'fields': ('is_active', 'is_staff',)}),
    )


class StdUAdmin(admin.ModelAdmin):
    list_display=('name','student_id','phone','get_username','academic_status')
    list_filter=('student_id','phone','academic_status',)
    search_fields=('student_id','phone','academic_status',)
    exclude = ['user',]

    @admin.display(ordering='user__username', description='Username')
    def get_username(self, obj):
        return obj.user.username if obj.user else 'N/A'
    

    def save_model(self, request, obj, form, change):
        if not obj.user:
            user = User(username=obj.student_id)
            user.set_password(obj.dob.strftime('%d%m%y'))
            user.email = obj.email
            user.save()
            obj.user = user

        return super().save_model(request, obj, form, change)


class StdCAdmin(admin.ModelAdmin):
    list_display=('name','student_id','phone','get_username','academic_status')
    list_filter=('student_id','phone','academic_status',)
    search_fields=('student_id','phone','academic_status',)
    exclude = ['user',]

    @admin.display(ordering='user__username', description='Username')
    def get_username(self, obj):
        return obj.user.username if obj.user else 'N/A'

    def save_model(self, request, obj, form, change):
        if not obj.user:
            user = User(username=obj.student_id)
            user.set_password(obj.dob.strftime('%d%m%y'))
            user.email = obj.email
            user.save()
            obj.user = user

        return super().save_model(request, obj, form, change)

class EnrollAdmin(admin.ModelAdmin):
    list_display=('student','enroll_year', 'enroll_semester','get_course_code','get_course_name')
    list_filter=('student__student_id','course__course_code','course__course_name','enroll_year', 'enroll_semester',)
    search_fields=('student__student_id','course__course_code','course__course_name','enroll_year', 'enroll_semester',)
    @admin.display(ordering='course__course_code', description='Course Code')
    def get_course_code(self, obj):
        return obj.course.course_code if obj.course else 'N/A'

    @admin.display(ordering='course__course_name', description='Course Name')
    def get_course_name(self, obj):
        return obj.course.course_name if obj.course else 'N/A'

class CourseAdmin(admin.ModelAdmin):
    list_display=('department','course_code', 'course_name',)
    list_filter=('department','course_code', 'course_name',)
    search_fields=('department','course_code', 'course_name',)

class ResultAdmin(admin.ModelAdmin):
    list_display=('student','enroll_course','grade_point','grade_letter',)
    list_filter=('student__student_id','enroll_course__course__course_code','enroll_course__course__course_name','enroll_course__enroll_year','enroll_course__enroll_semester')
    search_fields = ['student__student_id','enroll_course__course__course_code']

class FinancialUAdmin(admin.ModelAdmin):
    list_display = ('student','payment_date','payment_amount','money_receipt_no',)
    list_filter = ('student__student_id','money_receipt_no',)
    search_fields = ('student__student_id','money_receipt_no',)

class FinancialCAdmin(admin.ModelAdmin):
    list_display = ('student','payment_date','payment_amount','money_receipt_no',)
    list_filter = ('student__student_id','money_receipt_no',)
    search_fields = ('student__student_id','money_receipt_no',)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)

admin.site.register(StudentRegistrationUni,StdUAdmin)
admin.site.register(StudentRegistrationCollage,StdCAdmin)
admin.site.register(Enroll, EnrollAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Result,ResultAdmin)
admin.site.register(FinancialUni, FinancialUAdmin)
admin.site.register(FinancialCollege, FinancialCAdmin)