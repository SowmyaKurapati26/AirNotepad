import cv2
import numpy as np
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Canvas for drawing
canvas = np.ones((720, 1280, 3), dtype=np.uint8) * 255

# Video capture
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Width
cap.set(4, 720)   # Height

prev_x, prev_y = 0, 0
drawing = False

def fingers_up(hand_landmarks):
    fingers = []

    # Tip landmarks for fingers
    tip_ids = [4, 8, 12, 16, 20]

    # Thumb (tip.x < pip.x for right hand)
    fingers.append(hand_landmarks.landmark[tip_ids[0]].x < hand_landmarks.landmark[tip_ids[0] - 1].x)

    # Other fingers
    for i in range(1, 5):
        fingers.append(hand_landmarks.landmark[tip_ids[i]].y < hand_landmarks.landmark[tip_ids[i] - 2].y)

    return fingers

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            lm = hand_landmarks.landmark
            h, w, _ = frame.shape
            index_finger_tip = (int(lm[8].x * w), int(lm[8].y * h))

            fingers = fingers_up(hand_landmarks)

            # If only index finger is up -> Drawing mode
            if fingers[1] and not any(fingers[2:]):
                if not drawing:
                    prev_x, prev_y = index_finger_tip
                    drawing = True
                cv2.line(canvas, (prev_x, prev_y), index_finger_tip, (0, 0, 0), 5)
                prev_x, prev_y = index_finger_tip

            # If all fingers are up (open palm) -> Clear screen
            elif all(fingers):
                canvas = np.ones((720, 1280, 3), dtype=np.uint8) * 255
                drawing = False

            else:
                drawing = False

    # Overlay the canvas on webcam
    combined = cv2.addWeighted(frame, 0.5, canvas, 0.5, 0)
    cv2.imshow("AirNotepad", combined)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
