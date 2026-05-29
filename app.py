import cv2
import time
from ultralytics import YOLO

# ---------------- LOAD MODEL ----------------
model = YOLO("yolov8n.pt")

# ---------------- CAMERA ----------------
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("❌ Camera not working")
    exit()

cv2.namedWindow("🚀 AI Surveillance System", cv2.WINDOW_NORMAL)

# ---------------- SETTINGS ----------------
ALERT_PERSON_COUNT = 3
IMPORTANT_OBJECTS = ["cell phone", "laptop"]

# ---------------- VARIABLES ----------------
prev_time = 0
object_counts = {}
unique_ids = set()
track_history = {}

# ---------------- MAIN LOOP ----------------
while True:
    ret, frame = cap.read()

    if not ret:
        print("❌ Failed to grab frame")
        break

    frame = cv2.resize(frame, (900, 600))

    results = model.track(frame, persist=True)

    annotated_frame = frame.copy()

    object_counts.clear()
    person_count = 0
    alerts = []

    if results[0].boxes is not None:
        boxes = results[0].boxes

        if boxes.id is not None:
            for i in range(len(boxes.cls)):
                cls = int(boxes.cls[i])
                track_id = int(boxes.id[i])
                class_name = model.names[cls]

                object_counts[class_name] = object_counts.get(class_name, 0) + 1
                unique_ids.add(track_id)

                if class_name == "person":
                    person_count += 1

                x1, y1, x2, y2 = map(int, boxes.xyxy[i])
                cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

                # ---------------- TRACK HISTORY ----------------
                if track_id not in track_history:
                    track_history[track_id] = []

                track_history[track_id].append((cx, cy))

                if len(track_history[track_id]) > 20:
                    track_history[track_id].pop(0)

                # Draw trail
                for j in range(1, len(track_history[track_id])):
                    cv2.line(annotated_frame,
                             track_history[track_id][j - 1],
                             track_history[track_id][j],
                             (255, 0, 255), 2)

                # ---------------- COLOR LOGIC ----------------
                color = (0, 255, 0)

                if class_name in IMPORTANT_OBJECTS:
                    color = (0, 0, 255)

                # Draw box
                cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), color, 2)

                label = f"{class_name} ID:{track_id}"
                cv2.putText(annotated_frame, label,
                            (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, color, 2)

    # ---------------- ALERT SYSTEM ----------------
    if person_count > ALERT_PERSON_COUNT:
        alerts.append("⚠️ Too many people!")

    for obj in IMPORTANT_OBJECTS:
        if obj in object_counts:
            alerts.append(f"🚨 {obj} detected!")

    # ---------------- FPS ----------------
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time) if prev_time != 0 else 0
    prev_time = curr_time

    # ---------------- DISPLAY INFO ----------------
    y_offset = 30

    for obj, count in object_counts.items():
        cv2.putText(annotated_frame, f"{obj}: {count}",
                    (10, y_offset),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (0, 255, 0), 2)
        y_offset += 25

    cv2.putText(annotated_frame, f"Unique Objects: {len(unique_ids)}",
                (10, y_offset + 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (255, 255, 0), 2)

    cv2.putText(annotated_frame, f"FPS: {int(fps)}",
                (10, y_offset + 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (0, 255, 255), 2)

    # ---------------- ALERT DISPLAY ----------------
    alert_y = 400
    for alert in alerts:
        cv2.putText(annotated_frame, alert,
                    (10, alert_y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (0, 0, 255), 3)
        alert_y += 30

    # ---------------- SHOW WINDOW ----------------
    cv2.imshow("🚀 AI Surveillance System", annotated_frame)

    key = cv2.waitKey(1)

    if key == 27:  # ESC key
        break

    if cv2.getWindowProperty("🚀 AI Surveillance System", cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()