from django.shortcuts import render,redirect
from .forms import StudentRegistrationForm

# Create your views here.

def home(request):
    return render(request,template_name='home.html')

def student_registration(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = StudentRegistrationForm()

    return render(request, 'reg.html', {'form': form})
