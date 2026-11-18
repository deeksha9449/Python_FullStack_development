from django.shortcuts import render
from django.http import HttpResponse

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
