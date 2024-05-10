

from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import FileField
from django.contrib import messages
from django.urls import reverse
from .models import Student , Thesis
from django.conf import settings  # สำหรับจัดการเส้นทางไฟล์
import os  # สำหรับการจัดการไฟล์
import PyPDF2

def index(request):
     latest_students = Student.objects.all()[:10]
     latest_thesis = Thesis.objects.all()[:5]
     context = {
        'latest_students': latest_students,
        'latest_thesis': latest_thesis,
     }
     return render(request, 'index.html', context)

def students_list(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'students_list.html', context)

def add_student(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            student_id = request.POST['student_id']
            email = request.POST['email']
            major = request.POST['major']
            faculty = request.POST['faculty']
            
            new_student = Student.objects.create(name=name, student_id=student_id, email=email, major=major, faculty=faculty)
            
            return HttpResponseRedirect(reverse('students_list'))
        except KeyError:
            return HttpResponse("Invalid data")
        except Exception as e:
            return HttpResponse(f"Error: {e}")
    else:
        return render(request, 'add_students.html')
        
def add_record(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            student_id = request.POST['student_id']
            email = request.POST['email']
            major = request.POST['major']
            faculty = request.POST['faculty']
            
            new_student = Student.objects.create(name=name, student_id=student_id, email=email, major=major, faculty=faculty)
            
            return HttpResponseRedirect(reverse('students_list'))
        except KeyError:
            return HttpResponse("Invalid data")
        except Exception as e:
            return HttpResponse(f"Error: {e}")
    else:
        return HttpResponse("Method not allowed")
    

def edit_record(request, id):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            student_id = request.POST['student_id']
            email = request.POST['email']
            major = request.POST['major']
            faculty = request.POST['faculty']
            
            mystudent = Student.objects.get(id=id)
            mystudent.name = name
            mystudent.student_id = student_id
            mystudent.email = email
            mystudent.major = major
            mystudent.faculty = faculty
            mystudent.save()
            
            return HttpResponseRedirect(reverse('students_list'))
        except KeyError:
            return HttpResponse("Invalid data")
        except Exception as e:
            return HttpResponse(f"Error: {e}")
    else:
        return HttpResponse("Method not allowed")
    
def edit_student(request, id): 
    try:
        mystudent = Student.objects.get(id=id)
        if request.method == 'POST':
            name = request.POST['name']
            student_id = request.POST['student_id']
            email = request.POST['email']
            major = request.POST['major']
            faculty = request.POST['faculty']
            
            mystudent.name = name
            mystudent.student_id = student_id
            mystudent.email = email
            mystudent.major = major
            mystudent.faculty = faculty
            mystudent.save()
            
            return HttpResponseRedirect(reverse('students_list'))
        else:
            context = {'mystudent': mystudent}
            # แก้ไข reverse เพื่อระบุ id ของนักศึกษา
            edit_url = reverse('edit_student', args=[id])
            return render(request, 'edit_student.html', {'mystudent': mystudent, 'edit_url': edit_url})
    except Student.DoesNotExist:
        return HttpResponse("Student not found.")
    

def delete_student(request, id):
    try:
        student = Student.objects.get(id=id)
        student.delete()
        return redirect(reverse('students_list'))
    except Student.DoesNotExist:
        return HttpResponse("Student not found.")

def upload_thesis(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        advisor = request.POST['advisor']
        abstract = request.POST['abstract']
        keywords = request.POST['keywords']
        document = request.FILES['document']

        # ตรวจสอบประเภทไฟล์
        if document.content_type not in ['application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'application/pdf']:
            messages.error(request, "ประเภทไฟล์ไม่ถูกต้อง")
            return redirect('upload_thesis')

        # บันทึกข้อมูลลงฐานข้อมูล
        thesis = Thesis.objects.create(
            title=title,
            author=author,
            advisor=advisor,
            abstract=abstract,
            keywords=keywords,
            document=document
        )

        messages.success(request, "อัปโหลดวิทยานิพนธ์สำเร็จ")
        return redirect('upload_thesis')

    return render(request, 'upload_thesis.html')


def convert_thesis(request):
    # ... code to convert Word to PDF
    return HttpResponse('Conversion completed!')

def check_format(request):
    # ... code to check thesis format
    return HttpResponse('Format checked!')

def download_thesis(request):
    # ... code to download thesis
    return HttpResponse('Thesis downloaded!')

def delete_thesis(request, id):
    # ... code to delete thesis
    return HttpResponse('Thesis deleted!')

def search_thesis(request):
    if request.method == 'GET':
        search_term = request.GET.get('q')
        if not search_term:
            return render(request, 'search_thesis.html', {'error': 'กรุณาป้อนคำค้นหา'})

        # ค้นหาเอกสารวิทยานิพนธ์ตามคำค้นหา
        from django.db.models import Q
        thesis = Thesis.objects.filter(
            Q(title__icontains=search_term) |
            Q(abstract__icontains=search_term) |
            Q(keywords__icontains=search_term)
        )

        # แสดงผลการค้นหา
        context = {
            'thesis': thesis, 
            'search_term': search_term
        }

        return render(request, 'search_thesis.html', context)

    else:
        return HttpResponse("Method not allowed")

def detail_thesis(request, thesis_id):
    try:
        thesis = Thesis.objects.get(id=thesis_id)
        context = {'thesis': thesis}
        return render(request, 'thesis_detail.html', context)
    except Thesis.DoesNotExist:
        return HttpResponse("Thesis not found.")


