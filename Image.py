import cv2
import mediapipe as mp


img_path = "./Images/testImage2.jpg"
img = cv2.imread(img_path)

mp_face_detection = mp.solutions.face_detection
H, W, _ = img.shape


with mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.6
) as face_detection:
    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    results = face_detection.process(img_bgr)
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
            cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 3)

            # Bluring the Face
            img[y1 : y1 + h, x1 : x1 + w] = cv2.blur(
                img[y1 : y1 + h, x1 : x1 + w], (70, 70)
            )
            
    img = cv2.resize(img,(600,600))
    cv2.imshow("Face Detection", img)
    cv2.waitKey(0)
