from django.shortcuts import render,HttpResponse
from .models import student ,studenthistory #  the model is named Student

from django.contrib.auth.forms import UserCreationForm  #for form aythontication 
# Create your views here.



def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        course = request.POST.get('course')

        if not name or not email or not phone or not city or not course:
            return HttpResponse("All fields are required!")
        else:
            try:
                inputdata = student(
                    name=name,
                    email=email,
                    phone=phone,
                    city=city,
                    course=course
                )
                
                inputdata.save()

                history = studenthistory(
                    name=name,
                    email=email,
                    phone=phone,
                    city=city,
                    course=course
                )
                history.save()

                return HttpResponse("Record added successfully")
            except Exception as e:
                print(e)  
                return render(request, 'view.html', {"error": "An error occurred while saving the record"})
                
    return render(request, 'add.html')

    
def update(request,id):
    metadata=student.objects.filter(id=id).values()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        course = request.POST.get('course')
        user = student.objects.filter(id=id)
        user.update(
            name=name,
            email=email,
            phone=phone,
            city=city,
            course=course
            )      
        return HttpResponse("Record Updated successfully")
    return render(request,'update.html', { 'data' : metadata })

def view(request):
    data= student.objects.all().values()
    return render(request,'view.html',{'inputdata':data})
    
def delete(request, id):
    dt=student.objects.filter(id=id)
    dt.delete()
    return render(request,'delete.html')

def history(request):
    data= studenthistory.objects.all().values()
    return render(request,'history.html',{'inputdata':data})
def ragister(request):
    if request.mathod == "POST":
        form=UserCreationForm (request.POST)
 
def login(request):
    pass
def logout(request):
    pass
