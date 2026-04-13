import shutil
import os
import cv2
import numpy as np
from ultralytics import YOLO
from fastapi import FastAPI, File, UploadFile, Depends, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from sqlalchemy import Column, Integer, Float, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session



# Initialize database url

baseURL = 'sqlite:///./test.db'
engine = create_engine(baseURL, connect_args={'check_same_thread': False})
session_local = sessionmaker(bind=engine, autocommit=False, autoflush=False)

base = declarative_base()


# call model, app, and file folder

model = YOLO('best.pt')

app = FastAPI()

directory = 'static'
os.makedirs(directory, exist_ok=True)


# init db tables and db dependencies

class Log(base):
    __tablename__ = 'logs'
    id= Column(Integer, index=True, primary_key=True)
    name= Column(String)
    address= Column(String)
    sq_feet=Column(Float)

base.metadata.create_all(bind=engine)

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

def get_area(result):
    r = result[0]
    try:
        mask = r.masks[0].cpu().numpy()
        pixels = np.sum(mask.data) 
        pixels = int(pixels)
        pixels_to_sqmeters = 1/20
        meters = pixels*pixels_to_sqmeters
        meters_to_sqfeet = 3
        sqfeet = meters_to_sqfeet*meters
    except TypeError:
        sqfeet = 0
    return sqfeet

# endpoints

app.mount('/static', StaticFiles(directory=directory), 'static')
app.add_middleware(
    CORSMiddleware,
    allow_methods=['*'],
    allow_headers=['*'],
    allow_origins=['*']
)

@app.post('/static')
def add_file(file: UploadFile = File(...), 
            #  name: str = Form(), address: str = Form(), db: Session = Depends(get_db)
             ):
    file_path = os.path.join(directory, 'new.jpg')
    old_file_path = os.path.join(directory, 'old.jpg')

    with open(old_file_path, mode='wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = model.predict(old_file_path, conf=.03)

    result[0].save(file_path)


    sqfeet = get_area(result)

    # new_entry = Log(name=name, address=address)
    # db.add(new_entry)
    # db.commit()
    # db.refresh(new_entry)

    return {'url': 'http://localhost:8000/static/new.jpg',
            'sq_feet': sqfeet
            # , 'name': name, 'address': address, 'id': new_entry.id
            }

@app.put('/static')
def change_confidence(conf: float = Form()):
    old_path = 'static/old.jpg'
    file_path = os.path.join(directory, 'new.jpg')
    results = model.predict(old_path, conf=conf)
    sqfeet = get_area(results)
    results[0].save(file_path)
    return{'url': 'http://localhost:8000/static',
           'sq_feet': sqfeet}
    

@app.delete('/static')
def remove_file():
    if os.path.exists('static/new.jpg'):
        os.remove('static/new.jpg')
    return 'success'

@app.get('/static')
def get_logs(db: Session = Depends(get_db)):
    return db.query(Log).all()