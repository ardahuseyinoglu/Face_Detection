import cv2
from findProportionOfAreas import findProp

arda_cascade = cv2.CascadeClassifier('cascade.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
font = cv2.FONT_HERSHEY_COMPLEX

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ardas = arda_cascade.detectMultiScale(gray, 1.3, 5)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    arda_found = 0
    for (x,y,w,h) in faces:
        flag = 0
        if arda_found == 0:
            for (ax,ay,aw,ah) in ardas:
                print(findProp(x,y,w,h,ax,ay,aw,ah))
                if findProp(x,y,w,h,ax,ay,aw,ah) > 0.80:
                    cv2.putText(frame, 'Arda', (x-4,y-4), font, 0.5, (0,255,255), 1, cv2.LINE_AA)
                    cv2.rectangle(frame, (ax,ay), (ax+aw, ay+ah), (255,0,0), 2)
                    arda_found = 1
                    flag = 1
                    break

        if arda_found == 1 and flag == 1:
            continue
        else:
            cv2.putText(frame, 'Unknown', (x-4,y-4), font, 0.5, (0,255,255), 1, cv2.LINE_AA)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)


    cv2.imshow('img', frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break


cap.release()
cv2.destroyAllWindows()
