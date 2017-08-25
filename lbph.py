import cv2
from cv2 import *
import numpy as np
import os
import time
dir = os.listdir('trainingdata')
faces = []
labels = []
for i in range(len(dir)):
    filedir = ''.join(['/Users/CurtisMason/Desktop/code/PYTHON/vision/trainingdata/', dir[i]])
    cv2Obj = np.empty([8])
    faces.append(cv2.imread(filedir, 0))
    print filedir
    labels.append(1)
faces.append(cv2.imread(''.join(['/Users/CurtisMason/Desktop/code/PYTHON/vision/', 'blank.jpg']), 0))
labels.append(0)
faces.append(cv2.imread(''.join(['/Users/CurtisMason/Desktop/code/PYTHON/vision/', 'practice.jpg']), 0))
labels.append(0)
print 'finish'
print len(labels)
print len(faces)
subjects = ["unregistered", "Curtis Mason"]
face_recognizer = cv2.face.createLBPHFaceRecognizer()
face_recognizer.train(faces, np.array(labels))
start_time = time.time()
labely = face_recognizer.predict(cv2.imread(''.join(['/Users/CurtisMason/Desktop/code/PYTHON/vision/', 'trial.jpg']), 0))
print 'Elapsed Time: ', time.time()-start_time
if labely != 1:
    labely = 0
    print 'not found'
label_text = subjects[labely]

print(label_text)