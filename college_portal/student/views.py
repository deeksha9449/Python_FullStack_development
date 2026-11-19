from django.shortcuts import render
from django.http import HttpResponse
from .models import Student_table

# Create your views here.
def home(request):
    data={
        'name':"Sandy",
        'age':19,
        'department':"BCA"
    }
    marks=[100,90,99,90]
    return render(request,'home.html',{'data':data,'marks':marks})
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def forms(request):
    if request.method=="POST":
        reg_no=request.POST.get('reg_no')
        name=request.POST.get('name')
        marks=request.POST.get('marks')
        email=request.POST.get('email')
        dob=request.POST.get('dob')
        Student_table.objects.create(reg_no=reg_no,name=name,email=email,marks=marks,dob=dob)
        return HttpResponse("Saved Successfully")
    return render(request,'student_form.html')


