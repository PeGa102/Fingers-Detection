# Hand Detection with Finger Identification and Recording

This project demonstrates a Python application that uses a webcam to detect hands, identify individual fingers with unique colors, and record the video feed. The program uses the `cvzone` and `opencv-python` libraries for hand detection and real-time visualization.

---

## **Features**

1. **Hand Detection**:
   - Detects hands in real-time using `cvzone.HandTrackingModule`.

2. **Finger Identification**:
   - Identifies each finger (Thumb, Index, Middle, Ring, Pinky) and highlights it with a unique color:
     - **Thumb**: Red
     - **Index**: Green
     - **Middle**: Blue
     - **Ring**: Cyan
     - **Pinky**: Magenta

3. **Real-Time Labels**:
   - Displays the name of each finger near the corresponding detection point.

4. **Automatic Video Recording**:
   - Saves the video feed to a specified directory.
   - Records video automatically upon starting the program.

5. **Configurable Save Location**:
   - Videos are saved to the `C:\Users\pedri\OneDrive\Documentos\Projeto GPT\saving_record` directory.
   - Creates the folder automatically if it doesn't exist.

6. **Simple Exit Mechanism**:
   - Press **`q`** to stop the program and save the recording.

---

## **Requirements**

- Python 3.10 or newer.
- A webcam or external camera.

### **Python Libraries**

- `opencv-python`
- `cvzone`

You can install the required libraries by running:

```bash
pip install opencv-python cvzone
```

---

## **Setup and Usage**

1. Clone or download this repository.

2. Ensure Python and the required libraries are installed.

3. Run the `hand_detection.py` script:

   ```bash
   python hand_detection.py
   ```

4. The program will:
   - Open the webcam feed.
   - Detect hands and highlight fingers with unique colors.
   - Record the video feed automatically.

5. Press **`q`** to stop recording and exit the program.

6. Check the saved video in the directory:

   ```
   C:\Users\pedri\OneDrive\Documentos\Projeto GPT\saving_record
   ```

---

## **File Structure**

```
project-folder/
│
├── hand_detection.py    # Main Python script
├── README.md            # Project documentation
└── saving_record/       # Directory for saved video recordings (auto-created)
```

---

## **How It Works**

1. **Initialization**:
   - The script initializes the camera and the `cvzone` hand detector.

2. **Finger Detection**:
   - Detects hand landmarks and maps unique colors to each fingertip.

3. **Video Recording**:
   - Saves each frame to a video file using `cv2.VideoWriter`.

4. **User Interaction**:
   - Displays real-time detection and labels on the camera feed.
   - Stops recording when the user presses **`q`**.

---

## **Customization**

- **Save Location**:
  - Modify the `save_directory` variable in the script to change where videos are saved.

- **Detection Sensitivity**:
  - Adjust the `detectionCon` parameter in the `HandDetector` initialization for more or less sensitivity.

- **Colors**:
  - Edit the `colors` dictionary in the script to assign new colors to fingers.

---

## **Future Enhancements**

- Add support for detecting gestures.
- Enable multi-hand tracking with finger identification for each hand.
- Provide a GUI for easier interaction and settings configuration.

---

## **License**

Feel free to use and modify it as needed.

---

## **Author**

- **Name**: Pedro Gabriel Silva Macedo Machado.
- **Contact**: pedrocreed37@gmail.com

