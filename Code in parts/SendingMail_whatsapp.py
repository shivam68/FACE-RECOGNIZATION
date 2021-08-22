# Detecting FACE Infront and Sending EMAIL + WHATSAPP Message
###################################################################################################################################
## Using Facial Recognition..For Sending Mail!!     
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
def face_detector(img, size=0.5):
    # Convert image to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        return img, []
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (200, 200))
    return img, roi

# Open Webcam
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    image, face = face_detector(frame)
    try:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        results = vimal_model.predict(face)
        if results[1] < 500:
            confidence = int( 100 * (1 - (results[1])/400) )
            display_string = str(confidence) + '% Confident it is User'
        cv2.putText(image, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (255,120,150), 2)      
        if confidence >=85:
            if cv2.imwrite("detected.jpg",image):
                print("One Face Successfuly detected")
                print("try sending the Image via Mail...")
                send=send_email()
                if send == 0:
                    print("Email Send Succesfully\t\t",end=" ")
                    whatsapp=send_webwhatsapp()
                    if whatsapp == "Success":
                        print("you will Recieve Whatsapp Message soon...")
                else:
                    print("Something went wrong while sending you a Email...!!")
            break
        
        else:
            print("Come infront of the camera.....")
            
    except:
        print("No face found..Try again later")
        pass
        
    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break
        
cap.release()
cv2.destroyAllWindows()