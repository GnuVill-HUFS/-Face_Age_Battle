from PIL import Image, ImageFilter
import sys
import requests
import argparse
from collections import ChainMap


API_URL = 'https://kapi.kakao.com/v1/vision/face/detect'
MYAPP_KEY = '5da57c0ae4fcf77e767e2df44ca0bd62'

def detect_face(filename):
    headers = {'Authorization' : 'KakaoAK {}' .format(MYAPP_KEY)}

    try :
        files = { 'file' : open(filename, 'rb')}
        resp = requests.post(API_URL, headers=headers, files=files)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(str(e))
        sys.exit(0)

def mosaic(filename, detection_result):
    image = Image.open(filename)
    return image

def imageFind(requests):#request는 받는 사진 을 뜻함 "~.jpg"형식으로 받아야함 더블쿼테이션 필수
    if __name__ == "__main__":
        parser = argparse.ArgumentParser(description='Mosaic faces.')
        parser.add_argument('image_file', type=str, nargs='?', default=requests,
                            help='image file to hide faces')
        args = parser.parse_args()
        detection_result = detect_face(args.image_file)

        a={}
        a=detection_result['result']['faces']
        b= ChainMap(*a)
        c=b['facial_attributes']['gender']
        male=c['male']
        female=c['female']
        d=b['facial_attributes']
        age=d['age']
        score=b['score']

        face_info={'male':male, 'female':female,'age':age,'score':score}
        return(face_info)
#result,faces,facial_attribute,gender male 또는 female

#찬혁