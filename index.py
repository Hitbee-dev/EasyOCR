import easyocr
import cv2
import matplotlib.pyplot as plt
import math


image_name = "examples/kc_test28.png"
reader = easyocr.Reader(['ko','en']) # this needs to run only once to load the model into memory
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
            result3.append(j[:-1])
    result2.append(datas)


img = cv2.imread(image_name)
plot_datax = []
plot_datay = []
plot_legend = []
for n, i in enumerate(result2):
    buf = []
    # print(i)            # 레터박스 좌표(list)
    for m, j in enumerate(i):
        if m == 0 or m == 2:
            str_trans = j.split(", ")
            if len(str_trans[0]) > 5 or len(str_trans[1]) > 5:
                # 좌표가 소수점으로 들어오는 경우 방지
                arr_trans = []
                arr_trans.append(math.trunc(float(str_trans[0])))
                arr_trans.append(math.trunc(float(str_trans[1])))
                result_trans = arr_trans
            else:
                int_trans = map(int, str_trans)
                result_trans = list(int_trans)
            buf.append(result_trans)
    # print(result3[n])   # 결과값, 인식률(list)
    result4 = result3[n].split(", ")
    float_trans = float(result4[1])
    plot_datax.append(result4[0])
    plot_datay.append(float_trans*100)
    # plt.plot(result4[0], float_trans*100)
    # plot_legend.append(result4[0])

    if len(result4[0]) >= 6:
        # img = cv2.putText(img, result4[0], (buf[0][0]-35, buf[0][1]), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2, cv2.LINE_AA)
        img = cv2.rectangle(img, (buf[0][0], buf[0][1]), (buf[1][0], buf[1][1]), (0, 0, 255), 2)
    else:
        # img = cv2.putText(img, result4[0], (buf[0][0]-35, buf[0][1]), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2, cv2.LINE_AA)
        img = cv2.rectangle(img, (buf[0][0], buf[0][1]), (buf[1][0], buf[1][1]), (255, 0, 0), 2)

plt.bar(plot_datax, plot_datay, width=0.2, color = "black")
plt.xlabel('Number')
plt.ylabel('accuracy(%)')
# plt.legend(plot_legend)
plt.show()

cv2.imshow('test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

    