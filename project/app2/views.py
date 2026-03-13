from django.shortcuts import render, redirect
from .forms import StudentForm
from django.contrib import messages


def student_register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():
            student = form.save(commit=False)
            student.skills = ", ".join(form.cleaned_data['skills'])
            student.save()

            print("FORM SAVED SUCCESSFULLY")  # Debug line

            messages.success(request, "Student details saved successfully ✅")
            return redirect('success')
        
    else:
        form = StudentForm()

    return render(request, 'app2/register.html', {'form': form})

def success_page(request):
    return render(request, 'app2/success.html')