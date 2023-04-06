import cv2
import mediapipe as mp

# Initialize the hand landmark model
mp_hands = mp.solutions.hands

# Initialize the drawing utilities
mp_drawing = mp.solutions.drawing_utils

# Initialize the Hand Landmark model
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Read an image
image = cv2.imread('image.jpg')

# Convert the image to RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Process the image and get the hand landmarks
results = hands.process(image)

# Get the coordinates of the tip of the index finger
if results.multi_hand_landmarks:
    hand_landmarks = results.multi_hand_landmarks[0] # assuming only one hand is present in the image
    index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    x, y, z = index_finger_tip.x, index_finger_tip.y, index_finger_tip.z

# Draw the hand landmarks on the image
mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

# Display the image
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

