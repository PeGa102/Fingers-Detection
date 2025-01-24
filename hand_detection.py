import cv2
from cvzone.HandTrackingModule import HandDetector
import os
from datetime import datetime

def detect_fingers_and_record():
    # Initialize the camera and the hand detector
    cap = cv2.VideoCapture(0)
    detector = HandDetector(detectionCon=0.8, maxHands=2)

    # Check if the save directory exists, if not, create it
    save_directory = r"C:\Users\pedri\OneDrive\Documentos\Projeto GPT\saving_record"
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # Get the current timestamp for unique file naming
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    video_filename = os.path.join(save_directory, f"recording_{timestamp}.avi")

    # VideoWriter settings
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS)) or 30  # Default to 30 if FPS is unavailable
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec for .avi files
    out = cv2.VideoWriter(video_filename, fourcc, fps, (frame_width, frame_height))

    print("Recording started. Press 'q' to stop.")

    while True:
        success, img = cap.read()
        if not success:
            print("Failed to access the camera.")
            break

        # Detect hands
        hands, img = detector.findHands(img)

        # Define colors for each finger
        colors = {
            "Thumb": (0, 0, 255),   # Red
            "Index": (0, 255, 0),   # Green
            "Middle": (255, 0, 0),  # Blue
            "Ring": (255, 255, 0),  # Cyan
            "Pinky": (255, 0, 255)  # Magenta
        }

        if hands:
            for hand in hands:
                landmarks = hand['lmList']

                # Draw colored circles for each fingertip
                finger_names = ["Thumb", "Index", "Middle", "Ring", "Pinky"]
                finger_tips = [4, 8, 12, 16, 20]

                for i, finger_tip in enumerate(finger_tips):
                    finger_name = finger_names[i]
                    finger_color = colors[finger_name]

                    # Get the fingertip position
                    fingertip_pos = landmarks[finger_tip]

                    # Draw the circle on the fingertip
                    cv2.circle(img, (fingertip_pos[0], fingertip_pos[1]), 10, finger_color, -1)

                    # Display the finger name near the circle
                    cv2.putText(
                        img,
                        finger_name,
                        (fingertip_pos[0] + 20, fingertip_pos[1] + 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        finger_color,
                        2,
                        lineType=cv2.LINE_AA,
                    )

        # Write the frame to the video file
        out.write(img)

        # Display the camera feed with the overlay text
        cv2.imshow("Hand Detection with Finger Colors", img)

        # Stop the recording if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"Recording saved at {video_filename}")

if __name__ == "__main__":
    detect_fingers_and_record()
