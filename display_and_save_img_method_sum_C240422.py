############# method1  opencv ####################################
import cv2

# Load an image
image = cv2.imread("path/to/image.jpg")

# Display the image
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the image
cv2.imwrite("output_image.jpg", image)

#################################################################
############## mehod2 PIL      ##################################
from PIL import Image

# Open the image
image = Image.open("path/to/image.jpg")

# Display the image
image.show()

# Save the image
image.save("output_image.jpg")

#################################################################
############## mehod3 Matplotlib ################################
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load an image
image = mpimg.imread("path/to/image.jpg")

# Display the image
plt.imshow(image)
plt.axis('off')  # Hide axes
plt.show()

# Save the image
plt.imsave("output_image.jpg", image)

#################################################################