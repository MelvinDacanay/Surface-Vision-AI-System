from ultralytics import YOLO
import cv2
import numpy as np

# model = YOLO('yolov8n-seg.pt')
# model.train(data='C:/Users/sense/Documents/full stack 1/Model/data.yaml',
#             epochs=35,
#             imgsz=640,
#             batch=10,
#             patience=10,
#             )


model = YOLO('Model/best.pt')
result = model.predict('Model/val/images/Screenshot 2026-04-12 182607_png.rf.jn48MVhgM2kMCNIOVurp.png', 
              show=True,
              conf=.05,
              exist_ok=True
              )

result[0].save('Model/stats/new.jpg')

# for r in result:
mask = result[0].masks[0].cpu().numpy()

dw_pixels = np.sum(mask.data)

meters_per_pixel = 10/200
dw_meters = dw_pixels*meters_per_pixel



print(np.sum(mask.data), 'pixels')
print(dw_meters, 'meters')