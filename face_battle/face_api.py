import json
import sys
import argparse
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

with open('../Face_Age_Battle/KEY.json','r') as f:
    KEY = json.loads(f.read())

def get_KEY(name, KEY=KEY):
    try:
        return KEY['MYAPP_KEY']
    except:
        raise ImportError("KEY NAME : {0} is not matched".format(name))

API_URL = 'https://kapi.kakao.com/v1/vision/face/detect'
MYAPP_KEY = get_KEY('MYAPP_KEY')

def detect_face(filename):
    headers = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}

    try:
        files = { 'file' : open(filename, 'rb')}
        #files = { 'image_url' : filename}
        resp = requests.post(API_URL, headers=headers, files=files)
        resp.raise_for_status()

        #print(resp.json())
        return resp.json()
    except Exception as e:
        print(str(e))
        sys.exit(0)

def mosaic(filename, detection_result):
    image = Image.open(filename)

    for face in detection_result['result']['faces']:
        x = int(face['x']*image.width)
        w = int(face['w']*image.width)
        y = int(face['y']*image.height)
        h = int(face['h']*image.height)
        box = image.crop((x,y,x+w, y+h))
        box = box.resize((20,20), Image.NEAREST).resize((w,h), Image.NEAREST)
        image.paste(box, (x,y,x+w, y+h))

    return image



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Mosaic faces.')
    parser.add_argument('image_file', type=str, nargs='?',
                        default="./migrations/seka.jpg",
                        help='image file to hide faces')

    args = parser.parse_args()

    detection_result = detect_face(args.image_file)
    image = mosaic(args.image_file, detection_result)
    image.show()

    for i in range(4):
        print(detection_result['result']['faces'][i]['facial_attributes'])