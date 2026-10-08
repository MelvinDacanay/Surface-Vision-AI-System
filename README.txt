# Surface Vision AI

> **Computer Vision | Full-Stack AI Application | Python | YOLOv8 | FastAPI | React | SQLAlchemy**

## Project Summary

While working in the pressure-washing industry, I found that estimating and documenting the amount of cleanable surface at a job site could be time-consuming and subjective when done manually.

I wanted to build a computer vision application that could automatically identify concrete surfaces in job-site photos and provide a foundation for eventually estimating surface area and automating parts of the quoting process.

I built a full-stack computer vision application using **YOLOv8 segmentation**, a **FastAPI backend**, a **React frontend**, and **SQLite/SQLAlchemy** for data logging.

Users can upload job-site images, run them through the segmentation model, adjust the model's confidence threshold interactively, and view the processed output through the web interface.

I also implemented backend image processing, database logging, frontend/backend communication, and cache-busting logic to ensure users see the most recent processed image.

The result is an end-to-end AI application that takes an image from upload through model inference, stores information about the processing event, and returns a visual segmentation result to the user.

The application establishes the foundation for automatically estimating **concrete surface area**, which could eventually be used to improve pressure-washing quotes and job planning.

---

# 1. Project Overview

Surface Vision AI is a specialized computer vision application for the **pressure-washing and concrete-sealing industry**.

The application allows users to upload photographs of job sites and uses a **YOLOv8 segmentation model** to identify and isolate concrete surfaces.

The system combines machine learning with a web application so that the model can be used through an interactive interface rather than as an isolated Python script.

### Core Workflow

```text
User
  ↓
React Frontend
  ↓
Image Upload
  ↓
FastAPI Backend
  ↓
YOLOv8 Segmentation
  ↓
Processed Image
  ↓
Database Logging
  ↓
React Frontend
  ↓
Visual Result
```

---

# 2. Key Features

## Image Upload & Processing

The FastAPI backend accepts multipart image uploads and stores the images locally for model inference.

The backend then passes the image through the YOLOv8 segmentation model and returns the processed result.

---

## Interactive Confidence Thresholding

The React frontend provides a slider that allows users to adjust the model's confidence threshold.

This makes it possible to visually inspect how changing the confidence threshold affects the model's segmentation results without modifying the underlying model.

---

## Database Logging

The application uses **SQLAlchemy with SQLite** to log information about processed jobs.

The database records information such as:

* Client details
* Processed image paths
* Processing activity

This creates a persistent record of model usage rather than treating each inference as an isola
