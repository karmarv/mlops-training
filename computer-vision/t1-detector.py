# Databricks notebook source
# ! pip install --quiet -r https://raw.githubusercontent.com/ultralytics/yolov5/master/requirements.txt

# COMMAND ----------

import torch

# COMMAND ----------

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# COMMAND ----------

# Image
img = 'https://ultralytics.com/images/zidane.jpg'

# COMMAND ----------

# Inference
results = model(img)

# COMMAND ----------

results.pandas().xyxy[0]
