# 🖐️ Hand Gesture Recognition System

A real-time Hand Gesture Recognition System built using **Python**, **OpenCV**, and **MediaPipe**. This project detects hand landmarks through a webcam and enables gesture-based interaction with the system, including **volume control** and **media play/pause**.

---

## 📌 Project Overview

This project demonstrates real-time computer vision by detecting hand landmarks and recognizing simple hand gestures. The recognized gestures are mapped to system actions, providing a touch-free way to interact with multimedia controls.

---

## ✨ Features

- 🎥 Real-time hand detection using webcam
- 🖐️ 21 Hand Landmark Detection using MediaPipe
- 👍 Individual finger detection (Thumb, Index, Middle, Ring, Pinky)
- 🔊 Gesture-based System Volume Control
- ▶️ Open Palm Gesture → Play Media
- ⏸️ Closed Fist Gesture → Pause Media
- 📊 Real-time FPS Display
- 📈 Dynamic Volume Percentage Indicator

---

## 🛠️ Technologies Used

- Python 3.11
- OpenCV
- MediaPipe
- NumPy
- PyAutoGUI
- PyCAW
- COMTypes

---

## 📂 Project Structure

```
HandGestureRecognition/
│
├── HandDetectionModule.py     # Hand detection and landmark extraction
├── GestureControl.py          # Gesture detection module
├── VolumeControl.py           # Volume & media control application
├── test.py                    # Initial testing script
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/RC0809/Syntexchub_HandGestureRecognition.git
cd Syntexchub_HandGestureRecognition
```

### Install the dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python VolumeControl.py
```

Ensure your webcam is connected and accessible before running the application.

---

## 🎮 Gesture Controls

| Gesture | Action |
|----------|--------|
| 🖐️ Open Palm | Play Media |
| ✊ Closed Fist | Pause Media |
| 🤏 Thumb & Index Finger Distance | Increase / Decrease System Volume |

---

## 📸 Output

The application displays:

- Live webcam feed
- Hand landmarks
- Finger detection
- Volume bar
- Volume percentage
- FPS counter
- Gesture recognition status

---

## 🔮 Future Enhancements

- Next Track / Previous Track Gesture
- Brightness Control
- Mouse Cursor Control
- Virtual Drawing Application
- Multi-Hand Gesture Recognition
- Gesture-based Presentation Controller

---

## 📚 Learning Outcomes

This project helped in understanding:

- Computer Vision fundamentals
- Real-time image processing
- MediaPipe Hand Landmark Detection
- OpenCV image manipulation
- Gesture Recognition
- Human-Computer Interaction (HCI)

---

## 👨‍💻 Author

**Rakshit Chugh**

GitHub: https://github.com/RC0809

---

## 📄 License

This project is developed for learning and educational purposes.
