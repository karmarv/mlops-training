# Databricks notebook source
# MAGIC %md
# MAGIC # YoloV5 object detection model training 

# COMMAND ----------

# MAGIC %md
# MAGIC ## Setup 

# COMMAND ----------

! git clone https://github.com/ultralytics/yolov5  # clone
! pip install scikit-image -q

# COMMAND ----------

# MAGIC %cd yolov5
# MAGIC ! ls -l
# MAGIC ! pip install -qr requirements.txt

# COMMAND ----------

# Tensorboard  (optional)
%load_ext tensorboard
%tensorboard --logdir runs/train

# COMMAND ----------

# MAGIC %md
# MAGIC ## Train

# COMMAND ----------

# Train YOLOv5s on COCO128 for 2 epochs
! python train.py --img 640 --batch 16 --epochs 3 --data coco128.yaml --weights yolov5s.pt --cache

# COMMAND ----------

! ls -l ./runs/train/exp/weights

# COMMAND ----------

# MAGIC %md
# MAGIC ## Visualize 

# COMMAND ----------

! python detect.py --weights ./runs/train/exp/weights/best.pt --img 640 --conf 0.25 --source data/images

# COMMAND ----------

import matplotlib.pyplot as plt
from skimage import io
img = io.imread('runs/detect/exp/zidane.jpg')
plt.imshow(img)



# COMMAND ----------


