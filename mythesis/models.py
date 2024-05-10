from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):  # แก้ชื่อ model เป็น Student (ไม่ใช่ Students)
    name = models.CharField(max_length=255, verbose_name="ชื่อ")
    student_id = models.CharField(max_length=10, unique=True, verbose_name="รหัสนักศึกษา")
    email = models.EmailField(unique=True, verbose_name="อีเมล")
    major = models.CharField(max_length=255, verbose_name="สาขา")
    faculty = models.CharField(max_length=255, verbose_name="คณะ")

    def __str__(self):
        return self.name  # เพิ่มเมธอด __str__ เพื่อให้ชื่อของนักศึกษาแสดงในแอดมิน

class Thesis(models.Model):
    title = models.CharField(max_length=255, verbose_name="ชื่อเรื่องวิทยานิพนธ์")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="ผู้เขียน")
    advisor = models.CharField(max_length=255, verbose_name="อาจารย์ที่ปรึกษา")
    abstract = models.TextField(verbose_name="บทคัดย่อ")
    keywords = models.CharField(max_length=255, verbose_name="คำสำคัญ")
    document = models.FileField(upload_to='thesis/', verbose_name="ไฟล์เอกสาร")  
    upload_date = models.DateTimeField(auto_now_add=True, verbose_name="วันที่อัปโหลด")

    def __str__(self):
        return self.title  # เพิ่มเมธอด __str__ เพื่อให้ชื่อเรื่องวิทยานิพนธ์แสดงในแอดมิน
