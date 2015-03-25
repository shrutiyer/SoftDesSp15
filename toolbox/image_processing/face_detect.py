""" Experiment with face detection and image filtering using OpenCV 
            author: siyer
"""

import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('/home/shruti/SoftDes/SoftDesSp15/toolbox/image_processing/haarcascade_frontalface_alt.xml')
cap = cv2.VideoCapture(0)
kernel = np.ones((21,21),'uint8')

while(True):

    # Capture frame-by-frame
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20))
    for (x,y,w,h) in faces:
        #Blurs the face
    	frame[y:y+h,x:x+w,:] = cv2.dilate(frame[y:y+h,x:x+w,:], kernel)
        #Draw the eyes
    	cv2.circle(frame,(int(x+w/3),int(y+3*h/7)),15,(0,0,255),-1)
        cv2.circle(frame,(int(x+2*w/3),int(y+3*h/7)),15,(0,0,255),-1)
        #cv2.circle(frame,(int(x+w/3),int(y+3*h/7)+5,7,(0,0,0),-1)
        #cv2.circle(frame,(int(x+2*w/3),int(y+3*h/7)+5,7,(0,0,0),-1)
        #Draw the mouth
        cv2.ellipse(frame,(int(x+w/2),int(y+5*h/7)),(35,35),0,0,180,(0,0,0),8)
 	# Display the resulting frame
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
