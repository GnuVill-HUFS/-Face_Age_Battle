from django.shortcuts import render

def home(request):
    return render(request,'main.html')
    
def single_mode(request):
    return render(request,'single_mode.html')

def dual_mode(request):   
    return render(request,'dual_mode.html')

def mod_select(request):
    return render(request, 'mode_select.html')