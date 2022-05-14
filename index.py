import easyocr
import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
from PIL import Image

class easyocr_data():
    def init(image_name):
        global img_name
        # img_name = 'examples/kc_test31.jpg'
        img_name = image_name

    def image_origin():
        global image
        image = cv2.imread(img_name)
        cv2.imwrite(f"examples/boundary_result/result_1.jpg", image)
    ### 이미지 정규화

    def image_grayscale():
        global image_gray
        image_gray = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)
        cv2.imwrite(f"examples/boundary_result/result_2.jpg", image_gray)
        # cv2.imshow('gray', image_gray)

    def image_blur():
        global blur
        b,g,r = cv2.split(image)
        image2 = cv2.merge([r,g,b])
        blur = cv2.GaussianBlur(image_gray, ksize=(5,5), sigmaX=0)
        ret, thresh1 = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)
        cv2.imwrite(f"examples/boundary_result/result_3.jpg", blur)
        # cv2.imshow('blur', blur)

    def image_edged():
        global edged
        edged = cv2.Canny(blur, 10, 250)
        cv2.imwrite(f"examples/boundary_result/result_4.jpg", edged)
        # cv2.imshow('edged', edged)

    def image_closed():
        global closed
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10,10))
        closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
        cv2.imwrite(f"examples/boundary_result/result_5.jpg", closed)
        # cv2.imshow('closed', closed)

    def image_contours():
        global org_image
        contours, _ = cv2.findContours(closed.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        total = 0
        # 녹색 선으로 경계선 긋기
        contours_image = cv2.drawContours(image, contours, -1, (0,255,0), 3)
        cv2.imwrite(f"examples/boundary_result/result_6.jpg", contours_image)
        # cv2.imshow('contours_image', contours_image)

        contours_xy = np.array(contours)
        contours_xy.shape
        x_min, x_max = 0,0
        value = list()
        for i in range(len(contours_xy)):
            for j in range(len(contours_xy[i])):
                value.append(contours_xy[i][j][0][0]) #네번째 괄호가 0일때 x의 값
        x_min = min(value)
        x_max = max(value)
        print(f"x_min: {x_min}")
        print(f"x_max: {x_max}")
        
        # y의 min과 max 찾기
        y_min, y_max = 0,0
        value = list()
        for i in range(len(contours_xy)):
            for j in range(len(contours_xy[i])):
                value.append(contours_xy[i][j][0][1]) #네번째 괄호가 0일때 x의 값
        y_min = min(value)
        y_max = max(value)
        print(f"y_min: {y_min}")
        print(f"y_max: {y_max}")

        # image 자르기
        x = x_min
        y = y_min
        w = x_max-x_min
        h = y_max-y_min

        print(f"w: {w}, h: {h}")

        img_trim = image[y:y+h, x:x+w]
        cv2.imwrite('examples/org_trim.jpg', img_trim)
        cv2.imwrite(f"examples/boundary_result/result_7.jpg", img_trim)
        org_image = cv2.imread('examples/org_trim.jpg')
        # cv2.imshow('org_image', org_image)

    def image_normalization():
        # 자른 이미지에서 꼭지점 4개 검출
        gray = cv2.cvtColor(org_image, cv2.COLOR_RGB2GRAY)
        ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
        binary = cv2.bitwise_not(binary)
        contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_KCOS)
        tx_list = []
        ty_list = []
        for contour in contours:
            epsilon = cv2.arcLength(contour, True) * 0.02
            approx_poly = cv2.approxPolyDP(contour, epsilon, True)
            for approx in approx_poly:
                tx, ty = tuple(approx[0])
                tx_list.append(tx)
                ty_list.append(ty)
            
        tx_min = min(tx_list)
        tx_max = max(tx_list)
        ty_min = min(ty_list)
        ty_max = max(ty_list)

        tx_min_ty = ty_list[tx_list.index(tx_min)]   # tx_min 값의 ty값
        tx_max_ty = ty_list[tx_list.index(tx_max)]   # tx_max 값의 ty값
        ty_min_tx = tx_list[ty_list.index(ty_min)]   # ty_min 값의 tx값
        ty_max_tx = tx_list[ty_list.index(ty_max)]   # ty_max 값의 tx값

        print(f"tx_min: {tx_min, tx_min_ty}, tx_max: {tx_max, tx_max_ty}, ty_min: {ty_min_tx, ty_min}, ty_max: {ty_max_tx, ty_max}")
        print(tx_min, tx_max, ty_min, ty_max)
        cv2.circle(org_image, (tx_min, tx_min_ty), 3, (0, 0, 255), -1)
        cv2.circle(org_image, (tx_max, tx_max_ty), 3, (0, 0, 255), -1)
        cv2.circle(org_image, (ty_min_tx, ty_min), 3, (0, 0, 255), -1)
        cv2.circle(org_image, (ty_max_tx, ty_max), 3, (0, 0, 255), -1)
        cv2.imwrite(f"examples/boundary_result/result_8.jpg", org_image)
        # cv2.imshow("src", org_image)

        # 좌표 저장
        pts = np.zeros((4, 2), dtype=np.float32)
        pts_cnt = 0
        pts[0] = [tx_min, tx_min_ty]
        pts[1] = [tx_max, tx_max_ty]
        pts[2] = [ty_min_tx, ty_min]
        pts[3] = [ty_max_tx, ty_max]

        # 좌표 4개 중 상하좌우 찾기
        sm = pts.sum(axis=1)  # 4쌍의 좌표 각각 x+y 계산
        diff = np.diff(pts, axis=1)  # 4쌍의 좌표 각각 x-y 계산

        topLeft = pts[np.argmin(sm)]  # x+y가 가장 값이 좌상단 좌표
        bottomRight = pts[np.argmax(sm)]  # x+y가 가장 큰 값이 우하단 좌표
        topRight = pts[np.argmin(diff)]  # x-y가 가장 작은 것이 우상단 좌표
        bottomLeft = pts[np.argmax(diff)]  # x-y가 가장 큰 값이 좌하단 좌표

        # 변환 전 4개 좌표 
        pts1 = np.float32([topLeft, topRight, bottomRight, bottomLeft])

        # 변환 후 영상에 사용할 서류의 폭과 높이 계산
        w1 = abs(bottomRight[0] - bottomLeft[0])
        w2 = abs(topRight[0] - topLeft[0])
        h1 = abs(topRight[1] - bottomRight[1])
        h2 = abs(topLeft[1] - bottomLeft[1])
        width = max([w1, w2])  # 두 좌우 거리간의 최대값이 서류의 폭
        height = max([h1, h2])  # 두 상하 거리간의 최대값이 서류의 높이

        # 변환 후 4개 좌표
        pts2 = np.float32([[0, 0], [width - 1, 0],
                            [width - 1, height - 1], [0, height - 1]])

        # 변환 행렬 계산 
        mtrx = cv2.getPerspectiveTransform(pts1, pts2)

        # 원근 변환 적용
        result = cv2.warpPerspective(org_image, mtrx, (int(width), int(height)))
        # cv2.imshow('scanned', result)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        cv2.imwrite('examples/result.jpg', result)
        cv2.imwrite(f"examples/boundary_result/result_9.jpg", result)

    def image_crop( infilename , save_path):
        """
        image file 와 crop한이미지를 저장할 path 을 입력받아 crop_img를 저장한다.
        :param infilename:
            crop할 대상 image file 입력으로 넣는다.
        :param save_path:
            crop_image file의 저장 경로를 넣는다.
        :return:
        """
    
        img = Image.open( infilename )
        (img_h, img_w) = img.size
        print(img.size)
    
        # crop 할 사이즈 : grid_w, grid_h
        grid_w = math.ceil(img_w / 3) - 1 # crop width
        grid_h = math.ceil(img_h / 10) - 1 # crop height
        range_w = (int)(img_w/grid_w)
        range_h = (int)(img_h/grid_h)
        print(range_w, range_h)
    
        i = 0
        for w in range(range_w):
            for h in range(range_h):
                bbox = (h*grid_h, w*grid_w, (h+1)*(grid_h), (w+1)*(grid_w))
                print(h*grid_h, w*grid_w, (h+1)*(grid_h), (w+1)*(grid_w))
                # 가로 세로 시작, 가로 세로 끝
                crop_img = img.crop(bbox)
    
                fname = f"{i+1}.jpg"
                savename = save_path + fname
                crop_img.save(savename)
                print('save file ' + savename + '....')
                i += 1
    
    # image_crop('examples/result.jpg', 'examples/crops/')

    def image_result():
        for num in range(30):
            img = cv2.imread(f'examples/crops/{num+1}.jpg')
            ### EasyOCR
            reader = easyocr.Reader(['ko','en']) # this needs to run only once to load the model into memory
            final_data = reader.readtext(img) # 결과값 + 인식률 보이도록
            # final_data = reader.readtext('result', detail=0) # 결과값만 보이도록
            count = 0
            result2 = []
            result3 = []
            for i in final_data:
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

            # img = result
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

            # plt.bar(plot_datax, plot_datay, width=0.2, color = "black")
            # plt.xlabel('Number')
            # plt.ylabel('accuracy(%)')
            # plt.show()
            cv2.imwrite(f"examples/crops_result/result_{num+1}.jpg", img)

        v_img = cv2.imread(f"examples/crops_result/result_1.jpg")
        h_img = cv2.imread(f"examples/crops_result/result_1.jpg")
        addh = cv2.imread(f"examples/crops_result/result_1.jpg")
        for vcnt in range(3):       # 이미지 세로로 3장 이어붙힘
            for hcnt in range(10):  # 이미지 가로로 10장 이어붙힘
                if vcnt == 0:
                    pass
                elif vcnt == 1:
                    hcnt += 10
                elif vcnt == 2:
                    hcnt += 20
                    
                if hcnt == 0 or hcnt == 10 or hcnt == 20:
                    h_img = cv2.imread(f"examples/crops_result/result_{hcnt+1}.jpg")
                else:
                    bufh_img = cv2.imread(f"examples/crops_result/result_{hcnt+1}.jpg")
                    addh = cv2.hconcat([h_img, bufh_img])
                    cv2.imwrite(f"examples/adds_result/result_{hcnt}.jpg", addh)
                    h_img = addh
            if vcnt == 0:
                v_img = addh
            else:
                bufv_img = addh
                addv = cv2.vconcat([v_img, bufv_img])
                cv2.imwrite(f"examples/adds_result/add_result_{vcnt}.jpg", addv)
                v_img = addv
        cv2.imwrite(f"examples/boundary_result/result_10.jpg", v_img)
        cv2.imshow('result', v_img)

# easyocr_data.init('examples/kc_test31.jpg')
# easyocr_data.image_origin()
# easyocr_data.image_grayscale()
# easyocr_data.image_blur()
# easyocr_data.image_edged()
# easyocr_data.image_closed()
# easyocr_data.image_contours()
# easyocr_data.image_normalization()
# easyocr_data.image_crop('examples/result.jpg', 'examples/crops/')
# easyocr_data.image_result()

cv2.waitKey(0)
cv2.destroyAllWindows()