from django.shortcuts import render

def home(request):
    return render(request,'main.html')
    
def single_mode(request):
    return render(request,'single_mode.html')

def dual_mode(request):   
    return render(request,'dual_mode.html')

def mod_select(request):
    return render(request, 'mode_select.html')



def single_result(requests):

    picture =['pics']

    image_info = imageFind(picture)
    image_info = {'sex': None}


    image_info['age']=int(image_info['age'])


    if(image_info['male']>image_info['female']):
        image_info['sex']='남자'
    else if(image_info['male']<image_imfo['female']):
        image_info['sex']='여자'
    else:
        image_info['sex']='당첨'


    return render(requests, 'single_mode.html', image_info)

