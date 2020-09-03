# ELEC_20_DroneTroopers
### Tello_AirPro : A drone which will follow you where ever you go and keep you in center of the frame. 

### Commands that Drone can operate on using Speech Recognition:
  - You can control the drone movement by your speech commands. 
  - Such as takeoff, land, up, down, left and right. 

The DJI Tello drone Tello is a tiny and lightweight quadcopter created Ryze Robotics in collaboration with DJI and Intel Corporation. The quadcopter comes with some great features and electronics, including, among others, a 720p camera a vision system, barometer and range finder. What’s more, it’s programmable with the Scratch programming language and you can also create software applications. The drone comes with several accessories including a Quick Start Guide, four extra propellers, a propeller remover tool, and the battery, which is a 3.8V, two-cell battery, running at 1100mAh.

### INTERACTING WITH THE DRONE
using App of Tello.
using Keyboard(using Pygame Library)
using speech recognition (using Snowboy Hotword)

Pygame is a cross-platform set of Python modules designed for writing video games. It includes computer graphics and sound libraries designed to be used with the Python programming language.
We can use keyboard commands  on DJI Tello screen for implementing to control the directions of the drone.

Facial Recognition(using Haarcascades in OpenCV)
The drone will detect the face of the user and maintain some constant distance from the user kipping the user in center frame this feature can be exploited for side profiles.

The Viola–Jones object detection framework is the first object detection framework to provide competitive object detection rates in real-time proposed in 2001 by Paul Viola and Michael Jones. Although it can be trained to detect a variety of object classes, it was motivated primarily by the problem of face detection.

The main property of this algorithm is that training is slow, but detection is fast. This algorithm uses Haar basis feature filters, so it does not use multiplications.
Each face recognition filter (from the set of N filters) contains a set of cascade-connected classifiers. Each classifier looks at a rectangular subset of the detection window and determines if it looks like a face. If it does, the next classifier is applied. If all classifiers give a positive answer, the filter gives a positive answer and the face is recognized. Otherwise the next filter in the set of N filters is run.

Bounding Box:
We return bounding boxes coordinates for items that are detected in images. For example, the Detect Faces operation returns a bounding box for each face detected in an image. We use the bounding box coordinates to display a box around detected image For example, the following image shows a bounding box surrounding a face.


### SPEECH RECOGNITION USING SNOWBOY:
Snowboy is an embedded and real-time, always-listening but off-line, and highly customizable hotword detection engine that runs on Raspberry Pi, (Ubuntu) Linux, and Mac OS X. 
A hot word is a key word or phrase that a computer always listens for to trigger other actions. A hotword is also called a wake word or trigger word.


### **Steps to Run Code:**
1. You will need to run the FaceDetector.py first.
2. Then connect tello to your Laptop and run AirPro.py.
3. If you want tello to follow you, you can leave it here and comment out any speech recognition code    that might be causing crash of the program in the AirPro.py(most probably it will be commenting      the code which reads csv files ) but if you want the audio commands recognition to work then          install snowboy hotword first and but the files in the SpeechRecognition into it.
4. Code should run just fine !

