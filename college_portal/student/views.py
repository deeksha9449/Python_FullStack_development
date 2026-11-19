from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student_table
from .forms import Student_form_data

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
def student_form_dj(request):
    if request.method=="POST":
        form=Student_form_data(request.POST)
        if form.is_valid():
            reg_no1=form.cleaned_data['reg_no1']
            name1=form.cleaned_data['name1']
            email1=form.cleaned_data['email1']
            return HttpResponse("saved successfully")
        else:
            return HttpResponse("data not saved")
    else:
        form=Student_form_data()
        return render(request,'student_form_data.html',{'form':form})


