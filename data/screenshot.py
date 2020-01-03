#import libraries
import cv2
import os

#reading video
vid = cv2.VideoCapture('mario.mp4')

#create folder named data

try:
    
    if not os.path.exists('data'):
        os.makedirs('data')

except OSError:
    print('Error creating directory')

#get the current frame
currentframe = 0
count = 0

while(True):
    
    #read from frame

    ret, frame = vid.read()

    if ret:
        name = './data/frame' + str(currentframe) + '.jpg'

        #write extracted images
        cv2.imwrite(name, frame)

        #increasing counter for name
        currentframe += 1
        
        #increasing frame count
        count += 100
        vid.set(1, count)

    else:
        break

vid.release()
cv2.destroyAllWindows()
