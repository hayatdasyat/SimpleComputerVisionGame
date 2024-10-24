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

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/SimpleComputerVisionGame.git
