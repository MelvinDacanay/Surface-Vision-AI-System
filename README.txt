# PROJECT TITLE: Surface Vision AI
# TECH STACK: FastAPI, React, YOLOv8, SQLAlchemy, Python

1. PROJECT OVERVIEW
This application is a specialized computer vision tool designed for the surface renewal industry (pressure washing, concrete sealing). It allows users to upload photos of job sites and uses an integrated YOLOv8 segmentation model to automatically identify and isolate concrete surfaces.

2. KEY FEATURES
- Image Upload & Processing: FastAPI backend handles multi-part file uploads and stores them locally for model inference.
- Interactive Thresholding: A React-based slider allows users to tune the confidence level of the AI model on-the-fly.
- Database Logging: Automatic logging of client details and processed image paths using SQLAlchemy.
- Real-time Feedback: Frontend utilizes unique timestamps to bypass browser caching, ensuring the user sees the most recent AI-processed image.

3. TECHNICAL IMPLEMENTATION
- Backend: Built with FastAPI for high-performance asynchronous execution. Uses the Ultralytics library for YOLO model management.
- Frontend: Built with React, focusing on efficient state updates and Fetch API for backend communication.
- Database: SQLite database with a 'Log' table to track business activity and project data.

4. INSTALLATION
- Backend:
  1. Install dependencies: pip install fastapi uvicorn ultralytics sqlalchemy
  2. Run server: uvicorn main:app --reload
- Frontend:
  1. npm install
  2. npm start

5. FUTURE IMPROVEMENTS
- Integration of Area Calculation: Automatically calculating square footage based on pixel segmentation masks.
- Cloud Storage: Moving static files from local storage to AWS S3 for scalability.
- User Authentication: Adding login layers for multiple crew members to log jobs independently.