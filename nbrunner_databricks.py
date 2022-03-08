# Databricks notebook source
# MAGIC %md
# MAGIC ### Example for Detection in an Image
# MAGIC - https://scikit-image.org/docs/stable/auto_examples/applications/plot_face_detection.html 

# COMMAND ----------

from skimage import data
from skimage.feature import Cascade

import matplotlib.pyplot as plt
from matplotlib import patches


# COMMAND ----------

# MAGIC %md
# MAGIC ### Use pretrained Face Detector

# COMMAND ----------

# Load the trained file from the module root.
trained_file = data.lbp_frontal_face_cascade_filename()

# Initialize the detector cascade.
detector = Cascade(trained_file)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Load and image and run detector

# COMMAND ----------

img = data.astronaut()

# COMMAND ----------

detected = detector.detect_multi_scale(img=img,
                                       scale_factor=1.2,
                                       step_ratio=1,
                                       min_size=(60, 60),
                                       max_size=(123, 123))

# COMMAND ----------

# MAGIC %md
# MAGIC ## Plot the Results

# COMMAND ----------

plt.imshow(img)
img_desc = plt.gca()
plt.set_cmap('gray')

for patch in detected:
    img_desc.add_patch(
        patches.Rectangle(
            (patch['c'], patch['r']),
            patch['width'],
            patch['height'],
            fill=False,
            color='r',
            linewidth=2
        )
    )

plt.show()

# COMMAND ----------


