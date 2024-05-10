from django.urls import path
from . import views

urlpatterns = [
    # URL for the home page
    path('', views.index, name='index'),

    # URLs for students
    path('students/', views.students_list, name='students_list'),  # URL สำหรับแสดงรายชื่อนักศึกษา

    # URL for adding a new student
    path('students/add/', views.add_student, name='add_student'),  # แก้ชื่อ URL pattern เป็น 'add_student'
    path('students/add_record/', views.add_student, name='add_record'),  # URL สำหรับเพิ่มนักศึกษาใหม่ (ชื่อเดิมเพื่อรองรับความสมบูรณ์)

    # URL for editing an existing student
    path('students/edit/<int:id>/', views.edit_student, name='edit_student'),  # URL สำหรับแก้ไขข้อมูลนักศึกษา

    # URL for editing an existing student (original name for completeness)
    path('students/edit_record/<int:id>/', views.edit_record, name='edit_record'),  # URL สำหรับแก้ไขข้อมูลนักศึกษา (ชื่อเดิมเพื่อรองรับความสมบูรณ์)

    # URL for deleting an existing student
    path('students/delete/<int:id>/', views.delete_student, name='delete_student'),  # URL สำหรับลบข้อมูลนักศึกษา

    # URLs for theses
    path('upload_thesis/', views.upload_thesis, name='upload_thesis'),  # URL สำหรับอัปโหลดเอกสารวิทยานิพนธ์
    path('convert_thesis/', views.convert_thesis, name='convert_thesis'),  # URL สำหรับแปลงเอกสารวิทยานิพนธ์
    path('check_format/', views.check_format, name='check_format'),  # URL สำหรับตรวจสอบรูปแบบเอกสาร
    path('download_thesis/', views.download_thesis, name='download_thesis'),  # URL สำหรับดาวน์โหลดเอกสารวิทยานิพนธ์
    path('delete_thesis/<int:id>/', views.delete_thesis, name='delete_thesis'),  # URL สำหรับลบเอกสารวิทยานิพนธ์
    path('search_thesis/', views.search_thesis, name='search_thesis'),  # URL สำหรับค้นหาเอกสารวิทยานิพนธ์
    path('thesis/<int:thesis_id>/', views.detail_thesis, name='thesis_detail'),  # URL สำหรับแสดงรายละเอียดของเอกสารวิทยานิพนธ์
]
