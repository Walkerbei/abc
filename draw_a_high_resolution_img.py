import numpy as np
import cv2

# Define the dimensions of the image
width = 1920  # Width in pixels
height = 1080  # Height in pixels

# Create a white image
image = np.ones((height, width, 3), dtype=np.uint8) * 255  # White background

# Draw something on the image
cv2.rectangle(image, (100, 100), (500, 500), (0, 0, 0), 2)

# Save the image with high resolution
cv2.imwrite("high_res_image.png", image, [cv2.IMWRITE_PNG_COMPRESSION, 0])  # Lossless PNG format