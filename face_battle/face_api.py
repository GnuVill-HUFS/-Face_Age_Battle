def imageFind(requests):


    face_info = {}
    face_info['age']=None
    face_info['male']=None
    face_info['female']=None
    face_info['celebrity']=None
    """
    requests = ['image':이미지로컬저장위치] 라고 저장되어있음

    KAKAO 비전API의 얼굴인식을 사용합니다.

    face_info 변수에
    [나이정보, 성별 퍼센트, 닮은꼴]
    순서대로 age male female celebrity
    이 필요합니다.

    ** 선택사항
    PIL 라이브러리 이용하여 requests로 받은 이미지에 얼굴위치를
    (선으로) 적용시켜 사람들이 눈으로 볼 수 있게끔 이미지처리를 한다.
    """


    return face_info