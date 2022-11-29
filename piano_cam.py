import time,cv2
import mediapipe as mp
from math import floor
from playsound import playsound


def piyano():
    try:
        cap = cv2.VideoCapture ( 0 )
        mphands = mp.solutions.hands
        hands = mphands.Hands ( max_num_hands = 2 )
        mp_draw = mp.solutions.drawing_utils

        notes = { 6 : "SA" , 5 : "RI" , 4 : "GA" , 3 : "MA" , 2 : "PA" , 1 : "DHA" , 0 : "NI" }
        while True :
            success , img = cap.read ( )

            imgw = int ( img.shape [ 1 ] )
            imgh = int ( img.shape [ 0 ] )

            for i in range ( 10 , 150 * 8 , 150 ) :
                cv2.line ( img , (i , int ( 0.85 * imgh )) , (i , imgh) , (255 , 0 , 0) , 2 )
                if i == 10 :
                    cv2.line ( img , (i , int ( 0.85 * imgh )) , (150 * 7 + i , int ( 0.85 * imgh )) ,
                               (255 , 0 , 0) , 2 )

                # if i / 150 < 7:
                #    cv2.putText(img, notes[i / 150], (i + 20, int(0.15 * imgh)),
                #                cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 3)

            imgRGB = cv2.cvtColor ( img , cv2.COLOR_BGR2RGB )  # mp works with RGB image only
            results = hands.process ( imgRGB )  # recognizing hand

            if results.multi_hand_landmarks :
                for hand_loc in results.multi_hand_landmarks :
                    mp_draw.draw_landmarks ( img , hand_loc , mphands.HAND_CONNECTIONS )

                    tip = hand_loc.landmark [ mphands.HandLandmark.INDEX_FINGER_TIP ]
                    if 0.85 < tip.y < 0.89 and 110 < tip.x * imgw < 110 + 150 * 7 :
                        playsound ( notes [ floor ( (tip.x * imgw - 110) / 150 ) ] + ".mp3" )

            cv2.imshow ( "Image" , img )
            cv2.imshow ( "Image" , cv2.flip ( img , 1 ) )
            cv2.waitKey ( 1 )

    except:
        print('error')
        time.sleep(20),print(' waitied ...20 s trying again')
        piyano()



piyano()


