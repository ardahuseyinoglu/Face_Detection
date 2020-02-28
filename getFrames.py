import cv2
import os

def saveTo(path):

    if not os.path.exists(path):
        os.makedirs(path)
    os.chdir(path)

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    counter = 0
    numberOfImage = 0
    while True:
        ret, frame = cap.read()
        cv2.imshow('img', frame)

        if counter % 30 == 0:
            fileName = 'image_' + str(numberOfImage) + '.jpg'
            cv2.imwrite(fileName, frame)
            numberOfImage += 1

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

        counter += 1

    cap.release()
    cv2.destroyAllWindows()
