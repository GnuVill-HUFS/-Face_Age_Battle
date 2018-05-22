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


def dual_result(requests):

    picture1 =['pics1']
    picture2 =['pics2']

    image_info1 = imageFind(picture2)
    image_info1 = {'sex': None}
    image_info2 = imageFind(picture2)
    image_info2 = {'sex': None}


    image_info1['age']=int(image_info1['age'])
    image_info2['age']=int(image_info2['age'])


    if(image_info1['male']>image_info1['female']):
        image_info1['sex']='남자'
    else if(image_info1['male1']<image_imfo1['female']):
        image_info1['sex']='여자'
    else:
        image_info1['sex']='당첨'

    if(image_info2['male']>image_info2['female']):
        image_info2['sex']='남자'
    else if(image_info2['male1']<image_imfo2['female']):
        image_info2['sex']='여자'
    else:
        image_info2['sex']='당첨'

    image_return = {}
    image_return = {'picture1' : ['pics1'], 'picture2' : ['pics2'], 'age1' : image_info1['age'], 'age2' : image_info2['age'], 'sex1' : image_info1['sex'], 'sex2' : image_info2['sex']}


    return render(requests, 'dual_result.html', image_return)