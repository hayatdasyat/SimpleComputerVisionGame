# SimpleComputerVisionGame

An **Interactive Introduction to Computer Vision** game designed for students with no prior knowledge of the topic. This project allows students to engage with computer vision concepts through a fun and interactive guessing game.

## The Purpose

This game is designed to introduce students to the basics of computer vision by allowing them to participate in a real-time object detection game. It's intended for beginners and provides a hands-on learning experience in a classroom setting.

## How It Works

- The game uses a **YOLO model** to detect objects through a live webcam feed.
- The game displays a series of questions or clues about everyday objects (e.g., "I am used to store water and keep people hydrated" for a bottle).
- Students raise their hands to participate and come to the front to show their object to the camera.
- If the detected object matches the clue, the student wins, and the next round begins.

## Key Features

- **Real-time Object Detection**: Powered by YOLO, the game detects objects live from the camera feed.
- **Interactive Learning**: Students are engaged through a guessing game that helps them understand how computer vision systems recognize objects.
- **Simple Interface**: The game uses OpenCV to display the webcam feed and the current question, making it easy to interact with.



## Setup

Pre-requisite:
1. Install pycharm into your system. Follow this great instruction by kjdElectronics link:
   www.youtube.com/watch?v=0y5XlNeFxNk

Running the script: 
1. Download the script:
   **detection_of_object_game.py**
   
3. Move the script into your project directory it should look like this:
   **(C:\Users\<Username>\PycharmProjects\<your_project_name>\)**

4. In pycharm please install the required dependencies, use the terminal:
   **pip install ultralytics**

5. In pycharm's terminal you can run this command or click the run button:
   **python detection_of_object_game.py**
