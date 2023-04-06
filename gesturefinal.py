import mediapipe as mp
import cv2
import urllib.request
url="http://192.168.139.224/" #here we add IP address of NodeMCU
def sendRequest(url):
	n = urllib.request.urlopen(url) # send request to ESP

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
fingertips = [8, 12, 16, 20]

with mp_hands.Hands(min_detection_confidence=0.8, max_num_hands=1, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        h, w, c = frame.shape

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = cv2.flip(image, 1)
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                          mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                         )

        imageHeight, imageWidth, _ = image.shape

        if results.multi_hand_landmarks:
            for hand_Landmarks in results.multi_hand_landmarks:
                lm_list = []
                for id, lm in enumerate(hand_Landmarks.landmark):
                    lm_list.append(lm)

                finger_fold_status = []
                for tip in fingertips:
                    x,y =  int(lm_list[tip].x*w), int(lm_list[tip].y*h)

                    left_velocity = (int((lm_list[8].x - lm_list[0].x) * 100))
                    right_velocity = (int((lm_list[0].x - lm_list[8].x ) * 100))
                    forward_velocity = (int((lm_list[12].z - lm_list[0].z) * (-300)))

                    cv2.circle(image, (x , y) , 10 , (255, 0 ,0) ,cv2.FILLED)
                    cv2.putText(image, " ", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

                    if lm_list[tip].y > lm_list[tip - 3].y :
                        cv2.circle(image, (x, y), 10, (0, 0, 255), cv2.FILLED)
                        finger_fold_status.append(True)
                    else:
                        finger_fold_status.append(False)

                    if lm_list[12].x*100 > (lm_list[0].x*100 - 5) and lm_list[12].x*100 < (lm_list[0].x*100 + 3) and lm_list[12].z*300 > (lm_list[0].z*300 - 18) and (not all(finger_fold_status)):
                        cv2.putText(image, "Start", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 200, 0), 2)
                        cv2.circle(image, (x, y), 10, (0, 200, 0), cv2.FILLED)
                    elif all(finger_fold_status):
                        cv2.putText(image, "Stop", (20,30), cv2.FONT_HERSHEY_SIMPLEX, 1,(0 , 0 ,255), 2)
                        sendRequest(url + "/21")

                    elif lm_list[8].y < lm_list[5].y and lm_list[12].y < lm_list[9].y :
                        if  lm_list[12].x*100 > (lm_list[0].x*100 + 7) and lm_list[12].z * 300 > (lm_list[0].z * 300 -18):
                            cv2.putText(image, "Turn Right", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

                            y0 = int((-lm_list[8].y + lm_list[0].y) * 100)
                            x0 = int((lm_list[8].x - lm_list[0].x) * 100)
                            y1 = (2*y0) / 2
                            f = y1 / 5
                            if x0 >= f and x0 <= 2 * f:
                                cv2.putText(image, "Speed :" + "a", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                            (255, 0, 100), 2)
                                sendRequest(url + "/1")
                            elif x0 >= 2 * f and x0 <= 3 * f:
                                cv2.putText(image, "Speed :" + "b", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                            (255, 0, 100), 2)
                                sendRequest(url + "/2")
                            elif x0 >= 3 * f and x0 <= 4 * f:
                                cv2.putText(image, "Speed :" + "c", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                            (255, 0, 100), 2)
                                sendRequest(url + "/3")
                            elif x0 >= 4 * f and x0 <= 5 * f:
                                cv2.putText(image, "Speed :" + "d", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                            (255, 0, 100), 2)
                                sendRequest(url + "/4")
                            elif x0 >= 5 * f :
                                cv2.putText(image, "Speed :" + "e", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                            (255, 0, 100), 2)
                                sendRequest(url + "/5")
                        elif  lm_list[12].x*100 < (lm_list[0].x*100 - 7) and lm_list[12].z * 300 > (lm_list[0].z * 300 - 18):
                            cv2.putText(image, "Turn Left", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

                            y0 = int((-lm_list[8].y + lm_list[0].y) * 100)
                            x0 = int((lm_list[0].x - lm_list[8].x ) * 100)
                            y1 = (3*y0) / 2
                            f = y1 / 5
                            if x0 >= f and x0 <= 2 * f:
                                cv2.putText(image, "Speed :" + "a", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                            (255, 0, 100), 2)
                                sendRequest(url + "/6")
                            elif x0 >= 2 * f and x0 <= 3 * f:
                                cv2.putText(image, "Speed :" + "b", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                            (255, 0, 100), 2)
                                sendRequest(url + "/7")
                            elif x0 >= 3 * f and x0 <= 4 * f:
                                cv2.putText(image, "Speed :" + "c", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                            (255, 0, 100), 2)
                                sendRequest(url + "/8")
                            elif x0 >= 4 * f and x0 <= 5 * f:
                                cv2.putText(image, "Speed :" + "d", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                            (255, 0, 100), 2)
                                sendRequest(url + "/9")
                            elif x0 >= 5 * f :
                                cv2.putText(image, "Speed :" + "e", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                            (255, 0, 100), 2)
                                sendRequest(url + "/10")
                        elif lm_list[12].z*300 < (lm_list[0].z*300 - 15) and (not lm_list[4].x*100 < (lm_list[5].x*100 - 7)) :
                            cv2.putText(image, "Forward", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

                            y0 = int((-lm_list[8].y + lm_list[0].y) * 100)
                            x0 = int((lm_list[0].z - lm_list[8].z) * 100)
                            y1 = (y0) / 1.3
                            f = y1 / 5
                            if x0 >= f and x0 <= 2 * f:
                                cv2.putText(image, "Speed :" + "a", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                            (255, 0, 100), 2)
                                sendRequest(url + "/11")
                            elif x0 >= 2 * f and x0 <= 3 * f:
                                cv2.putText(image, "Speed :" + "b", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                            (255, 0, 100), 2)
                                sendRequest(url + "/12")
                            elif x0 >= 3 * f and x0 <= 4 * f:
                                cv2.putText(image, "Speed :" + "c", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                            (255, 0, 100), 2)
                                sendRequest(url + "/13")
                            elif x0 >= 4 * f and x0 <= 5 * f:
                                cv2.putText(image, "Speed :" + "d", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                            (255, 0, 100), 2)
                                sendRequest(url + "/14")
                            elif x0 >= 5 * f :
                                cv2.putText(image, "Speed :" + "e", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                            (255, 0, 100), 2)
                                sendRequest(url + "/15")
                        elif lm_list[12].z * 300 < (lm_list[0].z * 300 - 15) and lm_list[4].x*100 < (lm_list[5].x*100 - 7) :
                            cv2.putText(image, "Reverse", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

                            y0 = int((-lm_list[8].y + lm_list[0].y) * 100)
                            x0 = int((lm_list[0].z - lm_list[8].z) * 100)
                            y1 = (y0) / 1.3
                            f = y1 / 5
                            if x0 >= f and x0 <= 2 * f:
                                cv2.putText(image, "Speed :" + "a", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                            (255, 0, 100), 2)
                                sendRequest(url + "/16")
                            elif x0 >= 2 * f and x0 <= 3 * f:
                                cv2.putText(image, "Speed :" + "b", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                            (255, 0, 100), 2)
                                sendRequest(url + "/17")
                            elif x0 >= 3 * f and x0 <= 4 * f:
                                cv2.putText(image, "Speed :" + "c", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                            (255, 0, 100), 2)
                                sendRequest(url + "/18")
                            elif x0 >= 4 * f and x0 <= 5 * f:
                                cv2.putText(image, "Speed :" + "d", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                            (255, 0, 100), 2)
                                sendRequest(url + "/19")
                            elif x0 >= 5 * f :
                                cv2.putText(image, "Speed :" + "e", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                            (255, 0, 100), 2)
                                sendRequest(url + "/20")

        cv2.imshow('Hand Tracking', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
