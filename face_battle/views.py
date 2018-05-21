from django.shortcuts import render

def home(request):
    render(request,'main.html')
    
def single_mode(request):
    return render(request,'single_mode.html')

def dual_mode(request):   
    return render(request,'dual_mode.html')
