from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .face_api import imageFind

def home(request):
    return render(request,'main.html')
    
def single_mode(request):
    return render(request,'single_mode.html')

def dual_mode(request):   
    return render(request,'dual_mode.html')

def mod_select(request):
    return render(request, 'mode_select.html')

def main_page(requests):
    return render(requests, 'main.html')

def dual_result(requests):
    pass

def single_result(requests):
    image_info = imageFind()
    image_info['age'] = (int(image_info['age']))
    print(image_info)
    if (image_info['male'] > image_info['female']):
        image_info['sex'] = '남자'
    elif (image_info['male'] < image_info['female']):
        image_info['sex'] = '여자'
    else:
        image_info['sex'] = '당첨'
    #print(requests)

    return render(requests, './single_result.html', image_info)
