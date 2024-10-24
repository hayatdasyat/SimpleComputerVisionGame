import cv2
from ultralytics import YOLO

# Load YOLO model
yolo_model = YOLO("yolov8n.pt")

# Updated class mapping for object detection
class_mapping = {
    39: 'bottle',
    67: 'cell phone',
    24: 'backpack',
    63: 'laptop',
    64: 'mouse',
    26: 'handbag'
}

# List of questions corresponding to the objects in the same order
questions = [
    "WHAT AM I? I am often carried by people,",
    "and I help keep them hydrated on the go.",  # bottle
    "WHAT AM I? I fit in your hand,",
    "and connect you to people across the globe.",  # cell phone
    "WHAT AM I? I carry your daily essentials,",
    "and rest comfortably on your shoulders.",  # backpack
    "WHAT AM I? I help you work from anywhere,",
    "with my screen lighting up your tasks.",  # laptop
    "WHAT AM I? I move swiftly on a flat surface,",
    "and guide your digital actions with precision.",  # mouse
    "WHAT AM I? I hold your valuables close,",
    "while you go about your day with style."  # handbag
]

# Function to update the video feed
def update_video_feed(expected_class_id, question1, question2):
    ret, frame = cap.read()
    if ret:
        # Perform YOLO object detection
        yolo_results = yolo_model(frame, conf=0.5, classes=list(class_mapping.keys()))

        # Extract bounding box coordinates and class labels for objects
        for box, class_id in zip(yolo_results[0].boxes.xywh, yolo_results[0].boxes.cls):
            x_center, y_center, width, height = box
            x_min = int(x_center - width / 2)
            y_min = int(y_center - height / 2)
            x_max = int(x_center + width / 2)
            y_max = int(y_center + height / 2)

            # Draw the bounding box on the frame
            cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

            # Extract class ID
            class_id = int(class_id.item())

            # Get class name using class mapping dictionary
            class_name = class_mapping.get(class_id, 'Unknown')

            # Write class name on top of the bounding box
            cv2.putText(frame, class_name, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)

            # Check if the detected class ID matches the expected class ID
            if class_id == expected_class_id:
                cv2.putText(frame, "YOU WIN!", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 4)
                cv2.imshow("Video Feed", frame)
                # Wait for the user to press 'k' to go to the next question
                while True:
                    if cv2.waitKey(10) & 0xFF == ord('k'):
                        return True  # Return True to indicate that the object was correctly detected
                    if cv2.waitKey(10) & 0xFF == ord('q'):
                        return False  # Return False if 'q' is pressed

        # Draw black boxes behind the text for readability
        text_width1, text_height1 = cv2.getTextSize(question1, cv2.FONT_HERSHEY_SIMPLEX, 2.25, 4)[0]
        text_width2, text_height2 = cv2.getTextSize(question2, cv2.FONT_HERSHEY_SIMPLEX, 2.25, 4)[0]

        # Calculate box positions
        box1_start = (10, 100 - text_height1 - 10)  # Top left corner of the first box
        box1_end = (10 + text_width1 + 10, 100 + 10)  # Bottom right corner of the first box

        box2_start = (10, 150 - text_height2 - 10)  # Top left corner of the second box
        box2_end = (10 + text_width2 + 10, 150 + 10)  # Bottom right corner of the second box

        # Draw filled rectangles behind the text
        cv2.rectangle(frame, box1_start, box1_end, (0, 0, 0), cv2.FILLED)
        cv2.rectangle(frame, box2_start, box2_end, (0, 0, 0), cv2.FILLED)

        # Display the questions
        cv2.putText(frame, question1, (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 2.25, (255, 255, 255), 4)
        cv2.putText(frame, question2, (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 2.25, (255, 255, 255), 4)

        # Display the video feed
        cv2.imshow("Video Feed", frame)

    # Call this function again after 10 milliseconds
    if cv2.waitKey(10) & 0xFF == ord('q'):
        return False

# Open the default camera (0)
cap = cv2.VideoCapture(0)

# Set the camera resolution to 1080p
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

# Set the window to fullscreen
cv2.namedWindow("Video Feed", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Video Feed", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Loop through each object in the defined order
for expected_class_id, (question1, question2) in zip(class_mapping.keys(), zip(questions[0::2], questions[1::2])):
    while True:
        if update_video_feed(expected_class_id, question1, question2):
            break  # Break out of the loop to go to the next question

# Release video capture and close all windows
cap.release()
cv2.destroyAllWindows()
