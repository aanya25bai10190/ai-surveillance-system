# 🚀 AI Surveillance System (YOLOv8 + OpenCV)

A real-time **AI-powered object detection and tracking system** built using **YOLOv8** and **OpenCV**.
This project detects, tracks, and analyzes objects from a live webcam feed, making it suitable for surveillance and monitoring applications.

---

## 🔥 Features

* 🎥 **Real-time object detection** using YOLOv8
* 🧠 **Object tracking with unique IDs**
* 📊 **Live object count display**
* 🚨 **Alert system for important objects**
* 👤 **Crowd detection (person count threshold)**
* 🎯 **Motion trail visualization (tracking paths)**
* ⚡ **FPS monitoring for performance**
* 🖥️ **Clean OpenCV-based UI**

---

## 🛠️ Tech Stack

* **Python**
* **OpenCV**
* **Ultralytics YOLOv8**
* **NumPy**

---

## 📂 Project Structure

```
object-tracking-app/
│
├── app.py              # Main application
├── requirements.txt    # Dependencies
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/aanya25bai10190/ai-surveillance-system

cd ai-surveillance-system
```

### 2️⃣ Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```
python app.py
```

---

## ⚠️ Note on Model File

The YOLO model file (`yolov8n.pt`) is **not included in this repository** due to size constraints.

👉 It will be **automatically downloaded** when you run the application for the first time.

---

## 🎮 Controls

| Key | Action           |
| --- | ---------------- |
| ESC | Exit application |

---

## 🚨 Alerts System

* ⚠️ Triggers alert if too many people are detected
* 📱 Detects important objects like:

  * Cell phone
  * Laptop

---

## 🚀 Future Improvements

* 🔐 Face recognition system
* 📍 Zone-based intrusion detection
* 📸 Auto screenshot capture on alert
* 🔊 Alarm system integration
* 🌐 Web dashboard version

---

## 👩‍💻 Author

**Aanya Yadav**

---

## ⭐ Acknowledgements

* Ultralytics YOLOv8
* OpenCV community

---
