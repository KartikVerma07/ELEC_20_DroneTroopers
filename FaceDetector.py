
import cv2
import numpy
from dd import Tello
import numpy as np
import time
import datetime
import os
import csv
center_x = 480
center_y = 360

face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(r'haarcascade_eye.xml')
profile_cascade = cv2.CascadeClassifier(r'haarcascade_profileface.xml')


print("D_I_S_T_A_N_C_E \n X - Y - Z")
x_axis = 0

def run():

        #frame= cv2.cvtColor(cv2.imread(r"C:\\Users\\hp\\Desktop\\Sessions\\a\\tellocap0.jpg"), cv2.COLOR_BGR2RGB)
        while True:
                try:
                        
                        frame= cv2.cvtColor(cv2.imread(r"C:\Users\hp\Desktop\Sessions\a\\tellocap0.jpg"), cv2.COLOR_BGR2RGB)
                        img = frame
                        print("akshat")
                        img=cv2.flip( img, 1 )
                        cv2.circle(img,(480,360), 5, (0,255,0), -1)
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                        print(faces)
                        profile = profile_cascade.detectMultiScale(gray, 1.3, 5)
                        
                        if (faces !=()):
                                for (x,y,w,h) in faces:
                                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                                    roi_gray = gray[y:y+h, x:x+w]
                                    roi_color = img[y:y+h, x:x+w]
                                    bounding_centre_coordinates_x = int((x+x+w)/2)
                                    bounding_centre_coordinates_y = int((y+y+h)/2)
                                    cv2.circle(img,(bounding_centre_coordinates_x, bounding_centre_coordinates_y), 5, (255,0,0), -1)
                                    Area_z = int(h * w)
                                    Ideal_area=102.01
                                    print((-center_x+bounding_centre_coordinates_x), (center_y-bounding_centre_coordinates_y), ((-10201+Area_z)/100))
                                    x_axis = -center_x + bounding_centre_coordinates_x
                                    y_axis = center_y - bounding_centre_coordinates_y
                                    z_axis= int((-10201+Area_z)/100)

                                with open(r'C:\Users\hp\Desktop\\ginnovators.csv', 'w', newline='') as file:
                                    
                                    writer = csv.writer(file)
                                    writer.writerow([x_axis, y_axis, z_axis])
                        else:
                                with open(r'C:\Users\hp\Desktop\\ginnovators.csv', 'w', newline='') as file:
                                    
                                    writer = csv.writer(file)
                                    writer.writerow([0, 0, 0])
                        
                        #cv2.imshow('img',img)
                        
                        time.sleep(.25)
                except:
                        time.sleep(.25)
                        print("sorry")
                        pass


def main():  
    run()

if __name__ == '__main__':
    main()
