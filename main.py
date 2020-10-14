import cv2

cap = cv2.VideoCapture(0)
cv2.startWindowThread()

while True:
    ret, image = cap.read()
    face_cascade = cv2.CascadeClassifier('./venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=4,
        minSize=(10, 10)
    )
    faces_detected = "Detected: " + format(len(faces))
    print(faces_detected)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)

    cv2.imshow("camera", image)
    key = cv2.waitKey(100)
    if key == 27:  # Esc
        break

cap.release()
cv2.destroyAllWindows()
