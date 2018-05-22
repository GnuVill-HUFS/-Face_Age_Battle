from django.shortcuts import render
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

    picture =['pics']
    try:
        image_info = imageFind(picture)
        image_info = {'sex': None}

        image_info['age'] = int(image_info['age'])

        if (image_info['male'] > image_info['female']):
            image_info['sex'] = '남자'
        elif (image_info['male'] < image_info['female']):
            image_info['sex'] = '여자'
        else:
            image_info['sex'] = '당첨'
    except:
        image_info['age'] = "21"
        image_info['sex'] = "남자"



    return render(requests, 'single_result.html', image_info)

