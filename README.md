# Face Detection and Anonymizer

A Python-based real-time face detection and anonymization tool using OpenCV and Mediapipe. The program detects faces in a video stream, allows users to draw bounding boxes, and blur faces for anonymization.

---

## Features

- **Real-time Face Detection**: Detects faces from webcam input using Mediapipe's Face Detection API.
- **Bounding Box Toggle**: Draws a rectangle around detected faces when toggled.
- **Face Anonymization**: Blurs the detected face areas to ensure privacy.
- **User-Controlled Actions**: Toggle features dynamically with keyboard inputs.

---

## Requirements

Ensure you have the following installed before running the project:

- Python 3.7 or higher
- OpenCV
- Mediapipe

To install the required Python packages, run:

```bash
pip install opencv-python mediapipe
```

## How to use
1. Clone or download this repository.
2. Run the main.py file:
```bash
python video.py
```
3. Use the following keyboard inputs during runtime:
- Press d to toggle the face bounding box.
- Press b to toggle face blurring.
- Press q to quit the program.


## Customization
- Adjust the blur intensity by changing the kernel size in the cv2.blur() function.
- Modify the confidence threshold in min_detection_confidence for more precise face detection.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it.

