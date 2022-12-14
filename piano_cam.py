import cv2
import mediapipe as mp
from math import floor
from playsound import playsound
import pygame
pygame.init()
w,h = 90,110
x1,y1= 10,10
x2,y2 = 10+w,10
x3,y3 = 10+2*w,10
x4,y4 = 10+3*w,10
x5,y5 = 10+4*w,10
x6,y6 = 10+5*w,10
x7,y7 = 10+6*w,10
x8,y8 =10+7*w,10

cap = cv2.VideoCapture(0)
mphands = mp.solutions.hands
hands = mphands.Hands(max_num_hands = 1)
mp_draw = mp.solutions.drawing_utils

notes = {6 : "Do", 5 : "Re", 4 : "Mi", 3 : "Fa", 2 : "So", 1 : "La", 0 : "Si"}

while True:
    success, img = cap.read()

    imgw = int(img.shape[1])
    imgh = int(img.shape[0])

    for i in range ( 10 , 150 * 8 , 150 ) :
        cv2.line ( img , (i , int ( 0.85 * imgh )) , (i , imgh) , (255 , 0 , 0) , 2 )
        if i == 10 :
            cv2.line ( img , (i , int ( 0.85 * imgh )) , (150 * 7 + i , int ( 0.85 * imgh )) ,
                       (255 , 0 , 0) , 2 )


    imgRGB = cv2.cvtColor ( img , cv2.COLOR_BGR2RGB )  # mp works with RGB image only
    results = hands.process ( imgRGB )  # recognizing hand

    if results.multi_hand_landmarks :
        for hand_loc in results.multi_hand_landmarks :
            mp_draw.draw_landmarks ( img , hand_loc , mphands.HAND_CONNECTIONS )

            tip = hand_loc.landmark [ mphands.HandLandmark.INDEX_FINGER_TIP ]
            if 0.85 < tip.y < 0.89 and 110 < tip.x * imgw < 110 + 150 * 7 :
                pygame.mixer.Sound((notes[floor((tip.x * imgw - 110) / 150)] +'.wav' )).play ()

    #cv2.imshow("Image", img)
    cv2.imshow("Image", cv2.flip(img, 1))
    cv2.waitKey(1)



