# ✋ Air Notepad

Air Notepad is a computer vision–based virtual drawing application that allows users to write or draw in the air using hand gestures. It uses a webcam and **MediaPipe Hands** to track finger movements in real time and lets you draw without touching the screen.

---

## 🚀 Features

* 🖐️ Real-time hand tracking using MediaPipe
* ✍️ Draw in the air using **only the index finger**
* 🧹 Clear the canvas with an **open palm gesture**
* 🎥 Live webcam feed with drawing overlay
* 🖼️ Smooth and intuitive drawing experience

---

## 🧠 How It Works

* **Index finger up only** → Drawing mode
* **All fingers up (open palm)** → Clear the screen
* Any other gesture → Pause drawing

The drawing is done on a separate canvas which is blended with the live camera feed.

---

## 🛠️ Technologies Used

* Python 🐍
* OpenCV
* MediaPipe
* NumPy

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/SowmyaKurapati26/airnotepad.git
cd airnotepad
```

2. **Install dependencies**

```bash
pip install opencv-python mediapipe numpy
```

---

## ▶️ Usage

Run the Python script:

```bash
python air_notepad.py
```

### Controls

* ✍️ Raise only your **index finger** to draw
* 🧹 Show an **open palm** to clear the canvas
* ❌ Press **`q`** to exit the application

---



## 📁 Project Structure

```
air-notepad/
│
├── air_notepad.py
├── README.md
```

---

## ⚠️ Notes

* Ensure proper lighting for better hand detection
* Works best with one hand visible to the camera
* Designed primarily for **right-hand gestures**

---

## 🌟 Future Improvements

* Multiple colors and brush sizes
* Gesture-based undo/redo
* Save drawings as images
* Left-hand support

---

## 🧑‍💻 Author

Developed by **Sowmya Kurapati**
Feel free to contribute or suggest improvements!

---
