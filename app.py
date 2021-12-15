import cv2
import os
cam = cv2.VideoCapture("D:/Users/srinithi/Desktop/crime_detection/Chain snatching incident in New Delhi caught on camera.mp4")
    
try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')
    
currentframe = 0  
while(True):
    ret,frame = cam.read()  
    if ret:
        name = './data/frame' + str(currentframe) + '.jpg'
        print ('Creating...' + name)
  
        # writing the extracted images
        cv2.imwrite(name, frame)
  
        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    else:
        break
cam.release()
cv2.destroyAllWindows()