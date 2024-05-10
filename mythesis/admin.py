from django.contrib import admin
from .models import Student , Thesis

class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "student_id", "major", "faculty"]
    list_filter = ["name", "email", "major", "faculty"]
    search_fields = ["name", "email", "student_id", "major", "faculty"]

class ThesisAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "advisor", "abstract", "keywords", "document"]
    list_filter = ["title", "author", "advisor", "keywords", "document"]
    search_fields = ["title", "abstract", "keywords"]


admin.site.register(Student, StudentAdmin)
admin.site.register(Thesis, ThesisAdmin)

