from django.shortcuts import render
from django.http import HttpResponse
from form_app import forms
from form_app.models import Profile

# Create your views here.

def index(request):
    profile = Profile.objects.order_by('First_Name')
    return render(request, 'front.html', context={'profile':profile})

def final_page(request):
    return render(request, 'final.html', context=None)

def form_view_name(request):
    form = forms.New_Profile_Form()
    if request.method == 'POST':
        form = forms.New_Profile_Form(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return final_page(request)
        else:
            print('ERROR, FORM INVALID!')
        
    return render(request, "form.html", context={'form':form})