import cv2
import time
import numpy as np
import HandDetectionModule as hdm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import pyautogui

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0
detector = hdm.HandDetector()

devices = AudioUtilities.GetSpeakers()
interface = devices._dev.Activate(
    IAudioEndpointVolume._iid_,
    CLSCTX_ALL,
    None
)

volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]

volBar = 400
volPer = 0

cooldown = 0
media_state = "Paused"
tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()

    if not success:
        break

    detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        fingers = []

        if abs(lmList[4][1] - lmList[17][1]) > abs(lmList[3][1] - lmList[17][1]):
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        thumb = fingers[0]
        index = fingers[1]
        middle = fingers[2]
        ring = fingers[3]
        pinky = fingers[4]

        totalFingers = fingers.count(1)

        cv2.putText(img, f'Thumb: {thumb}', (400, 120),
                    cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 255), 2)
        cv2.putText(img, f'Index: {index}', (400, 150),
                    cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 255), 2)
        cv2.putText(img, f'Middle: {middle}', (400, 180),
                    cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 255), 2)
        cv2.putText(img, f'Ring: {ring}', (400, 210),
                    cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 255), 2)
        cv2.putText(img, f'Pinky: {pinky}', (400, 240),
                    cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 255), 2)

        if totalFingers == 5:
            cv2.putText(img, "Open Palm: Play", (120, 100),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)

            if media_state != "Playing" and time.time() - cooldown > 2:
                pyautogui.press("space")
                media_state = "Playing"
                cooldown = time.time()

        elif totalFingers == 0:
            cv2.putText(img, "Closed Fist: Pause", (120, 100),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)

            if media_state != "Paused" and time.time() - cooldown > 2:
                pyautogui.press("space")
                media_state = "Paused"
                cooldown = time.time()

        else:
            x1, y1 = lmList[4][1], lmList[4][2]
            x2, y2 = lmList[8][1], lmList[8][2]
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            cv2.circle(img, (cx, cy), 7, (0, 0, 255), cv2.FILLED)

            length = math.hypot(x2 - x1, y2 - y1)

            vol = np.interp(length, [50, 300], [minVol, maxVol])
            volBar = np.interp(length, [50, 300], [400, 150])
            volPer = np.interp(length, [50, 300], [0, 100])

            volume.SetMasterVolumeLevel(vol, None)

            if length < 50:
                cv2.circle(img, (cx, cy), 7, (0, 255, 0), cv2.FILLED)

    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
    cv2.putText(img, f'{int(volPer)} %', (40, 450),
                cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 1)

    cTime = time.time()
    fps = 1 / (cTime - pTime) if pTime != 0 else 0
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (10, 70),
                cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 2)

    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()