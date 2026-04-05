import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO
import time

model=YOLO('yolov8n.pt')


def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        colorsBGR = [x, y]
        print(colorsBGR)
        

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

cap=cv2.VideoCapture('Video_Vasos.mp4')

my_file = open("coco.txt", "r")
data = my_file.read()
class_list = data.split("\n")
   




area1=[(14,442),(212,443),(214,754),(14,755)]
area2=[(268,427),(431,425),(431,732),(269,733)]
area3=[(535,426),(695,426),(694,729),(534,728)]
area4=[(804,415),(998,415),(997,716),(804,716)]
area5=[(151,166),(301,166),(302,434),(151,435)]
area6=[(403,170),(522,169),(523,435),(401,434)]
area7=[(635,143),(757,143),(757,386),(636,386)]
area8=[(274,21),(394,18),(395,229),(282,231)]
area9=[(539,18),(648,20),(639,231),(535,227)]
area10=[(773,54),(893,53),(894,259),(771,259)]





while True:    
    ret,frame = cap.read()
    if not ret:
        break
    
    frame=cv2.resize(frame,(1020,800))

    results=model.predict(frame)
 #   print(results)
    a=results[0].boxes.data
    px=pd.DataFrame(a).astype("float")
#    print(px)
   
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list8 = []
    list9 = []
    list10 = []
   
    
    for index,row in px.iterrows():
#        print(row)
 
        x1=int(row[0])
        y1=int(row[1])
        x2=int(row[2])
        y2=int(row[3])
        d=int(row[5])
        c=class_list[d]
        if 'cup' in c:
            cx=int(x1+x2)//2
            cy=int(y1+y2)//2

       
      
            results1=cv2.pointPolygonTest(np.array(area1,np.int32),((cx,cy)),False)
            if results1>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list1.append(c)
            results2 = cv2.pointPolygonTest(np.array(area2, np.int32), ((cx, cy)), False)
            if results2 >= 0:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.circle(frame, (cx, cy), 3, (0, 0, 255), -1)
                list2.append(c)
            results3 = cv2.pointPolygonTest(np.array(area3, np.int32), ((cx, cy)), False)
            if results3 >= 0:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.circle(frame, (cx, cy), 3, (0, 0, 255), -1)
                list3.append(c)
            results4 = cv2.pointPolygonTest(np.array(area4, np.int32), ((cx, cy)), False)
            if results4 >= 0:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.circle(frame, (cx, cy), 3, (0, 0, 255), -1)
                list4.append(c)
            results5 = cv2.pointPolygonTest(np.array(area5, np.int32), ((cx, cy)), False)
            if results5 >= 0:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.circle(frame, (cx, cy), 3, (0, 0, 255), -1)
                list5.append(c)
            results6 = cv2.pointPolygonTest(np.array(area6, np.int32), ((cx, cy)), False)
            if results6 >= 0:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.circle(frame, (cx, cy), 3, (0, 0, 255), -1)
                list6.append(c)
            results7 = cv2.pointPolygonTest(np.array(area7, np.int32), ((cx, cy)), False)
            if results7 >= 0:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.circle(frame, (cx, cy), 3, (0, 0, 255), -1)
                list7.append(c)
            results8 = cv2.pointPolygonTest(np.array(area8, np.int32), ((cx, cy)), False)
            if results8 >= 0:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.circle(frame, (cx, cy), 3, (0, 0, 255), -1)
                list8.append(c)
            results9 = cv2.pointPolygonTest(np.array(area9, np.int32), ((cx, cy)), False)
            if results9 >= 0:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.circle(frame, (cx, cy), 3, (0, 0, 255), -1)
                list9.append(c)
            results10 = cv2.pointPolygonTest(np.array(area10, np.int32), ((cx, cy)), False)
            if results10 >= 0:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.circle(frame, (cx, cy), 3, (0, 0, 255), -1)
                list10.append(c)


    a1=(len(list1))
    a2=(len(list2))
    a3=(len(list3))
    a4=(len(list4))
    a5=(len(list5))
    a6=(len(list6))
    a7=(len(list7))
    a8=(len(list8))
    a9=(len(list9))
    a10=(len(list10))
    o = (a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10)
    space = (o)
    print(space)
  
    if a1==1:
        cv2.polylines(frame,[np.array(area1,np.int32)],True,(255,0,0),2)
        cv2.putText(frame,str('1'),(38,723),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)
    else:
        cv2.polylines(frame,[np.array(area1,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('1'),(38,723),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)

    if a2==1:
        cv2.polylines(frame,[np.array(area2,np.int32)],True,(255,0,0),2)
        cv2.putText(frame,str('2'),(294,703),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)
    else:
        cv2.polylines(frame,[np.array(area2,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('2'),(294,703),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    if a3==1:
        cv2.polylines(frame,[np.array(area3,np.int32)],True,(255,0,0),2)
        cv2.putText(frame,str('3'),(516,702),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)
    else:
        cv2.polylines(frame,[np.array(area3,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('3'),(516,702),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    if a4==1:
        cv2.polylines(frame,[np.array(area4,np.int32)],True,(255,0,0),2)
        cv2.putText(frame,str('4'),(775,683),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)
    else:
        cv2.polylines(frame,[np.array(area4,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('4'),(775,683),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    if a5==1:
        cv2.polylines(frame,[np.array(area5,np.int32)],True,(255,0,0),2)
        cv2.putText(frame,str('5'),(171,393),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)
    else:
        cv2.polylines(frame,[np.array(area5,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('5'),(171,393),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    if a6==1:
        cv2.polylines(frame,[np.array(area6,np.int32)],True,(255,0,0),2)
        cv2.putText(frame,str('6'),(388,379),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)
    else:
        cv2.polylines(frame,[np.array(area6,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('6'),(388,379),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    if a7==1:
        cv2.polylines(frame,[np.array(area7,np.int32)],True,(255,0,0),2)
        cv2.putText(frame,str('7'),(616,350),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)
    else:
        cv2.polylines(frame,[np.array(area7,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('7'),(616,350),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    if a8==1:
        cv2.polylines(frame,[np.array(area8,np.int32)],True,(255,0,0),2)
        cv2.putText(frame,str('8'),(255,58),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)
    else:
        cv2.polylines(frame,[np.array(area8,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('8'),(252,58),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    if a9==1:
        cv2.polylines(frame,[np.array(area9,np.int32)],True,(255,0,0),2)
        cv2.putText(frame,str('9'),(515,60),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)
    else:
        cv2.polylines(frame,[np.array(area9,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('9'),(515,60),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    if a10==1:
        cv2.polylines(frame,[np.array(area10,np.int32)],True,(255,0,0),2)
        cv2.putText(frame,str('10'),(744,60),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)
    else:
        cv2.polylines(frame,[np.array(area10,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('10'),(744,60),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)

    cv2.putText(frame, str(space), (23, 30), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 2)

    cv2.imshow("RGB", frame)

    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()
#stream.stop()


