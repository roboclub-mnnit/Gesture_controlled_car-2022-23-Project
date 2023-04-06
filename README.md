# Gesture_controlled_car-2022-23-Project
## About
This is a project based on hardware and OpenCV which is proposed and executed by robotics club of MNNIT to provide hands on experience and exposure to the students in different fields related to robotics.
![image](https://user-images.githubusercontent.com/130023827/230298919-71846126-458d-4e24-8479-0ad96877c274.png)

## Project mentors
| Name  | Branch | Registration No. |
| -------- | -------- | -------- |
| Anurag Gupta | Electronics and Communication Engineering | 20195168 |
| Purushotam Kumar Agrawal | Electrical Engineering |	20192042 |
| Gautam Kumar | Mechanical Engineering | 20203059 |
## Project Group Members
| Name | Branch | Registration No. |
| -------- | -------- | -------- |
| Shubham Verma | Mechanical Engineering | 20213132 |
| Sumit Mishra | Mechanical Engineering | 20213065 |
## Techstack
- Python
- Arduino Programming
- NodeMCU Programming
### Libraries to be installed/used 
- OpenCV
- Mediapipe
- URLlib Request
- ESP8266 Library (In ArduinoIDE)

## Components
|COMPONENT NAME |QUANTITY | DESCRIPTION |
| -------- | -------- | -------- |
| DC Motor | 2 | To rotate wheel |
| Wheels | 2 | To drive bot |
| Castor Wheel | 1 | To provide balance and movement |
| Arduino UNO | 1 | Microcontroller to drive motor driver |
| NodeMCU | 1 | To establish connection between PC and arduino |
| L298A motor driver| 1 | To control motor speed and direction  |
| Chasis | 1 | On this whole bot is made |
| BreadBoard | 1 | To make circuit connection |
| Jumper Wires | 9-10 | To complete circuit |
## Circuit Diagram
- For Arduino-NodeMCU connection we follow this connection,NodeMCU Rx is connected to Tx of Arduino and vice versa.Also connect ground of both and NodeMCU to
![image](https://user-images.githubusercontent.com/130023827/230319898-a2edb609-0a2e-46b1-98fb-fd2a2bcfb58e.png)
- For Arduino-MotorDriver connection we follow this
![image](https://user-images.githubusercontent.com/130023827/230362082-3256b84f-8008-4185-aa89-0a272fdf48d5.png)

## Implentation 
In this project, we have used wide range of functions of OpenCV and Mediapipe. Ranging from capturing gesture using camera to processing them in Arduino. Now we will have a look on the methodology.
- Firstly, we used the OpenCV library to open camera and get the images from user.
- In next step, we used the Mediapipe, which provides us with some predefined functions to set relations between positioning of fingers, in turn those relations were used to define the direction and velocity of bot.
- In Mediapipe, we have set velocity on the basis of distance between two fingers in 2D plane.
![image](https://user-images.githubusercontent.com/130023827/230366589-316a7fdb-c58e-4dc5-8c7b-787c99f5b9dc.png)
- We have set Turning on the basis of coordinate sign.
![image](https://user-images.githubusercontent.com/130023827/230367573-2cdb24ca-19da-4245-8715-0c1bbe3c21b0.png)
- Here we can see 'Speed c' , actually we have divided max speed in 5 divisions, namely 'a' to 'e'. With 'a' being lowest and 'e' being the maximum.
- Then we have send a string as per the required condition to Local host server, which in turn is accessed by NodeMCU. Then we establish a serial communication between Arduino and NodeMCU.
- We wrote Arduino code, as per the gestures and serial were passed to 'if-else' condition and motor was run.




