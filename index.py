import easyocr
image_name = "examples/kc.png"

reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
result = reader.readtext(image_name) # 결과값 + 인식률 보이도록
# result = reader.readtext('examples/kc.png', detail=0) # 결과값만 보이도록
count = 0
result2 = []
result3 = []
for i in result:
    count += 1
    data = str(i).split("],")
    datas = []
    for n, j in enumerate(data):
        if n == 0:
            datas.append(j[3:])
        elif n == 1 or n == 2:
            datas.append(j[2:])
        elif n == 3:
            datas.append(j[2:-1])
        else:
            result3.append(j)
    result2.append(datas)

# import cv2
# import numpy as np
# win_name = "EasyOCR"
# img = cv2.imread(image_name)
# cv2.imshow(win_name, img)
for n, i in enumerate(result2):
    print(i)            # 레터박스 좌표(list)
    print(result3[n])   # 결과값, 인식률(list)