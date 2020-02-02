# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 19:27:14 2019

@author: hp
"""
import cv2
import numpy
from djitellopy import Tello
import cv2
import pygame
from pygame.locals import *
import numpy as np
import time
import datetime
import os
import csv

center_x = 480
center_y = 360


# Speed of the drone
S = 20

# Frames per second of the pygame window display
FPS = 25
ddir = r"C:\\Users\\hp\\Desktop\\Sessions\\"

if not os.path.isdir(ddir):
    os.mkdir(ddir)


ddir = r"C:\\Users\\hp\\Desktop\\Sessions\\ {}".format(str(datetime.datetime.now()).replace(':','-').replace('.','_'))
ddir1=r"C:\\Users\\hp\\Desktop\\Sessions\\a\\"
os.mkdir(ddir)
if not os.path.isdir(ddir1):
    os.mkdir(ddir1)



    


print("D_I_S_T_A_N_C_E \n X - Y - Z")
x_axis = 0
class FrontEnd(object):
    """ Maintains the Tello display and moves it through the keyboard keys.
        Press escape key to quit.
        The controls are:
            - T: Takeoff
            - L: Land
                - Arrow keys: Forward, backward, left and right.
            - A and D: Counter clockwise and clockwise rotations
            - W and S: Up and down.
    """

    def __init__(self):
        # Init pygame
        pygame.init()

        # Creat pygame window
        pygame.display.set_caption("Tello video stream")
        self.screen = pygame.display.set_mode([960, 720])

        # Init Tello object that interacts with the Tello drone
        self.tello = Tello()

        # Drone velocities between -100~100
        self.for_back_velocity = 0
        self.left_right_velocity = 0
        self.up_down_velocity = 0
        self.yaw_velocity = 0
        self.speed = 10
        self.imgCount=0
        self.send_rc_control = False
        self.c=0
        self.g=0
        # create update timer
        pygame.time.set_timer(USEREVENT + 1, 50)
        self.set_var=0

    def run(self):

        if not self.tello.connect():
            print("Tello not connected")
            return

        if not self.tello.set_speed(self.speed):
            print("Not set speed to lowest possible")
            return

        # In case streaming is on. This happens when we quit this program without the escape key.
        if not self.tello.streamoff():
            print("Could not stop video stream")
            return

        if not self.tello.streamon():
            print("Could not start video stream")
            return
        
        frame_read = self.tello.get_frame_read()

        should_stop = False
        while not should_stop:

            for event in pygame.event.get():
                #if event.type == USEREVENT + 1:
                    #pass
                    #self.update()
                if event.type == QUIT:
                    should_stop = True
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        should_stop = True
                    else:
                        self.keydown(event.key)
                elif event.type == KEYUP:
                    self.keyup(event.key)

            if frame_read.stopped:
                frame_read.stop()
                break

            self.screen.fill([0, 0, 0])
            frame = cv2.cvtColor(frame_read.frame, cv2.COLOR_BGR2RGB)
            #frame = cv2.cvtColor(frame_read.frame)
            
            img_c=0
            cv2.imwrite("{}/tellocap{}.jpg".format(ddir,self.imgCount),frame)
            cv2.imwrite("{}/tellocap{}.jpg".format(ddir1,img_c),frame)
            self.imgCount=self.imgCount+1
            x_axis=0
            y_axis=0
            z_axis=0
            self.g=0
            command_arr = []
            
            print("yooooo start")
            try:
                with open(r"C:\Users\hp\Desktop\Tello\ubuntushare\\commands.csv")as f:
                    rows=csv.reader(f)
                    for command in rows:
                        command_arr.append(command)
                    print(command_arr)
                
            
            except:
                print("1st error")
            try:
                if(int(command_arr[1][0])==1):
                    print("land")
                    self.tello.land()
                    self.set_var=0
                    self.g=1
                    time.sleep(1/12)
                    
                    
                    
                    
                elif(int(command_arr[2][0])==2):
                    print("takeoff")
                    self.tello.takeoff()
                    self.set_var=1
                    self.g=1
                    
                    
                    
                elif(int(command_arr[3][0])==3):
                    print("left")
                    self.tello.send_control_command("left 30")
                    self.g=1
                    
                    
                    
                elif(int(command_arr[4][0])==4):
                    print("right")
                    self.tello.send_control_command("right 30")
                    self.g=1
                    
                    
                
                elif(int(command_arr[5][0])==5):
                    print("forward")
                    self.tello.send_control_command("forward 30")
                    self.g=1
                      
                    
                elif(int(command_arr[6][0])==6):
                    print("backward")
                    self.tello.send_control_command("back 30")
                    self.g=1
                    
                    
                with open(r"C:\Users\hp\Desktop\Tello\ubuntushare\\commands.csv", 'w') as fl:
                          writer = csv.writer(fl, delimiter=',')
                          fl.truncate(0)
                fl.close()
                
            except:
                print("error speech")
            
            if(self.g == 0):
                if(self.set_var==1):
                                        
                        
                    try:
                        with open(r"C:\Users\hp\Desktop\\ginnovators.csv", 'r') as csvfile: 
                            # creating a csv reader object 
                            csvreader = csv.reader(csvfile) 
                              
                            # extracting field names through first row 
                            for row in csvreader: 
                                values=row
                            print(values)
                        x_axis = int(values[0])
                        y_axis = int(values[1])
                        z_axis = int(values[2])
                    except:
                        print("csv error")
                    
                    try:
                        if( -50 < x_axis < 50):
                            
                            if(-38 < y_axis < 38):
                                
                                if(-7 < z_axis < 18):
                                    self.tello.send_rc_control(0,0,0,0)   
                                else:
                                    
                                    if(z_axis > 18):
                                        
                                        self.for_back_velocity = -30
                                        self.tello.send_rc_control(0,self.for_back_velocity,0,0)
                                        
                                    elif(z_axis < -7):
                                        
                                        self.for_back_velocity = 30
                                        self.tello.send_rc_control(0,self.for_back_velocity,0,0)
                            else:
                                if(y_axis>38):
                                    
                                    self.up_down_velocity = 30
                                    self.tello.send_rc_control(0,0, self.up_down_velocity,0)
                                    
                                elif(y_axis<-38):
                                    
                                    self.up_down_velocity = -30
                                    self.tello.send_rc_control(0,0, self.up_down_velocity,0)       
                        else:

                            if(x_axis > 50):
                                
                                self.yaw_velocity = -20
                                self.tello.send_rc_control(0,0,0,self.yaw_velocity)
                                
                            elif(x_axis < -50):
                                
                                self.yaw_velocity = 20
                                self.tello.send_rc_control(0,0,0,self.yaw_velocity)
                    except:
                        print("error")
                    
                    
                        
                frame = pygame.surfarray.make_surface(frame)
                self.screen.blit(frame, (0, 0))
                
                pygame.display.update()
                
                time.sleep(1/25)

        # Call it always before finishing. I deallocate resources.
        self.tello.end()

    def keydown(self, key):
        """ Update velocities based on key pressed
        Arguments:
            key: pygame key
        """
        if key == pygame.K_UP:  # set forward velocity
            self.for_back_velocity = S
        elif key == pygame.K_DOWN:  # set backward velocity
            self.for_back_velocity = -S
        elif key == pygame.K_LEFT:  # set left velocity
            self.left_right_velocity = -S
        elif key == pygame.K_RIGHT:  # set right velocity
            self.left_right_velocity = S
        elif key == pygame.K_w:  # set up velocity
            self.up_down_velocity = S
        elif key == pygame.K_s:  # set down velocity
            self.up_down_velocity = -S
        elif key == pygame.K_a:  # set yaw clockwise velocity
            self.yaw_velocity = -S
        elif key == pygame.K_d:  # set yaw counter clockwise velocity
            self.yaw_velocity = S

    def keyup(self, key):
        """ Update velocities based on key released
        Arguments:
            key: pygame key
        """
        if key == pygame.K_UP or key == pygame.K_DOWN:  # set zero forward/backward velocity
            self.for_back_velocity = 0
        elif key == pygame.K_LEFT or key == pygame.K_RIGHT:  # set zero left/right velocity
            self.left_right_velocity = 0
        elif key == pygame.K_w or key == pygame.K_s:  # set zero up/down velocity
            self.up_down_velocity = 0
        elif key == pygame.K_a or key == pygame.K_d:  # set zero yaw velocity
            self.yaw_velocity = 0
        elif key == pygame.K_t:  # takeoff
            self.tello.takeoff()
            self.set_var=1
            self.send_rc_control = True
        elif key == pygame.K_l:  # land
            self.tello.land()
            self.send_rc_control = False
            

    def update(self):
        """ Update routine. Send velocities to Tello."""
        if self.send_rc_control:
            self.tello.send_rc_control(self.left_right_velocity, self.for_back_velocity, self.up_down_velocity,
                                       self.yaw_velocity)


    


def main():
    frontend = FrontEnd()

    # run frontend
    frontend.run()


if __name__ == '__main__':
    main()

