import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mp_face_detection = mp.solutions.face_detection

detect = False
blur = False


with mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.6
) as face_detection:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        else:
            H, W, _ = frame.shape
            results = face_detection.process(frame)
            # print(results.detections)

            if results.detections is not None:
                for detections in results.detections:
                    location_data = detections.location_data
                    bbox = location_data.relative_bounding_box
                    # print(bbox)

                    x1, y1, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height

                    x1 = int(x1 * W)
                    y1 = int(y1 * H)
                    w = int(w * W)
                    h = int(h * H)

                    # Detecting Face and Drawing Rectangle
                    if detect:
                        cv2.rectangle(frame, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 3)

                    # Bluring the Face
                    if blur:
                        frame[y1 : y1 + h, x1 : x1 + w] = cv2.blur(
                            frame[y1 : y1 + h, x1 : x1 + w], (70, 70)
                        )

            cv2.imshow("Video", frame)
            key = cv2.waitKey(1)

            if key == ord("q"):
                break
            elif key == ord("d"):
                detect = not detect
            elif key == ord("b"):
                blur = not blur

cap.release()
cv2.destroyAllWindows
