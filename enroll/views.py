from django.shortcuts import render,HttpResponseRedirect
from .forms import studentRegistration
from .models import user
# Create your views here.

# this function wil add new item and show all items
def add_show(request):
 if request.method == 'POST':
  fm = studentRegistration(request.POST)
  if fm.is_valid():
      fm.save()
 else:
  fm = studentRegistration()
 stud = user.objects.all()
 return render(request, 'enroll/addandshow.html',{'form':fm,
'stu':stud})
 
 # this function will Update/Edit
 
def update_data(request,id):
  if request.method == 'POST':
   pi = user.objects.get(pk=id)
   fm = studentRegistration(request.POST, instance=pi)
   if fm.is_valid():
    fm.save() 
  else:
    pi = user.objects.get(pk=id)
    fm = studentRegistration(instance=pi)
  
  return render(request, 'enroll/updatestudent.html',{'form':fm})

#t this function will delete
def delete_data(request,id):
    if request.method == 'POST':
        pi = user.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    
    