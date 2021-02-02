import cv2
import sys

imgnum = 1
for i in range(300):
    try:
        image_file = (str(imgnum)+".jpg")
        cascade_file = "./haarcascade_frontalface_alt.xml"
        image = cv2.imread(image_file)
        image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cascade = cv2.CascadeClassifier(cascade_file)
        print(image_gs)
        face_list = cascade.detectMultiScale(image_gs,
                                             scaleFactor=1.1,
                                             minNeighbors=1,
                                             minSize=(30, 30))
    except Exception:
        continue
    if len(face_list) > 0:
        print(face_list)
        # color = (0, 0, 0)
        for face in face_list:
            x, y, w, h = face
            # cv2.rectangle(image, (x, y), (x+w, y+h), color, thickness=8)
            cropped = image[y - int(h/4):y + h + int(h/4), x -
                            int(w/4):x + w + int(w/4)]
            try:
                cv2.imwrite("cropped"+str(imgnum)+".png", cropped)
            except Exception:
                break
    else:
        print("no face")

    imgnum = imgnum + 1
