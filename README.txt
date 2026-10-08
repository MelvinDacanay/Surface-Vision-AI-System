# Surface Vision AI

> **Computer Vision | YOLOv8 | FastAPI | React | SQLAlchemy | Python**

## Project Summary

While working in the pressure-washing industry, I wanted to reduce the subjectivity and time involved in identifying the amount of concrete surface in job-site photos.

Build a computer vision application that could identify concrete surfaces and provide a foundation for eventually estimating surface area and improving job quotes.

I integrated a **YOLOv8 segmentation model** into a full-stack application using **FastAPI, React, and SQLAlchemy**. Users can upload job-site images, adjust the model's confidence threshold, view segmentation results, and log processed jobs in a SQLite database.

Built an end-to-end AI application that connects **image upload → model inference → database logging → visual results** through a web interface.

The project provides the foundation for eventually converting segmentation masks into **estimated square footage** for automated job estimation.

---

## Key Features

* **YOLOv8 segmentation** — identifies concrete surfaces in uploaded images
* **FastAPI backend** — handles image uploads, inference, and processed results
* **React frontend** — provides image upload, results, and confidence-threshold controls
* **SQLAlchemy + SQLite** — logs client and image-processing information
* **Cache busting** — ensures newly processed images are displayed instead of cached results

---

## Technical Architecture

```text
React
  ↓
FastAPI
  ↓
YOLOv8 Segmentation
  ↓
Processed Image
  ↓
SQLite / SQLAlchemy
  ↓
React
```

---

## Tech Stack

* Python
* YOLOv8 / Ultralytics
* FastAPI
* React
* SQLAlchemy
* SQLite

---

## Installation

### Backend

```bash
pip install fastapi uvicorn ultralytics sqlalchemy
uvicorn main:app --reload
```

### Frontend

```bash
npm install
npm start
```

---

## Future Work

* Convert segmentation masks into estimated square footage
* Add reference-based scaling for physical area estimation
* Move image storage to AWS S3
* Add user authentication and multi-crew support
* Migrate from SQLite to PostgreSQL for production use

---

## Limitations

* Segmentation accuracy depends on training data and image quality.
* Images currently lack a physical scale, so pixel area cannot directly determine square footage.
* Local storage and SQLite are intended for the current prototype.
* Authentication and production deployment have not yet been implemented.

---

## Project Goal

Turn:

**Job-Site Image → Concrete Segmentation → Square Footage → Job Estimate**

This project combines **computer vision, machine learning, full-stack development, and a real-world business application**.
