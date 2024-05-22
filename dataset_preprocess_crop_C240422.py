import os
import numpy as np
from PIL import Image
import torchvision.transforms as transforms
import matplotlib.pyplot as plt

# Define the preprocessing pipeline
def preprocess(image_path, annotation_path, output_size):
    # Load the image and annotation
    image = Image.open(image_path).convert("RGB")
    annotation = Image.open(annotation_path).convert("RGB")  # Example, assuming annotation is RGB image
    
    # Define transforms for cropping, resizing, and normalization
    transform = transforms.Compose([
        transforms.RandomCrop(output_size),  # Randomly crop regions
        transforms.Resize(output_size),      # Resize to desired output size
        transforms.ToTensor(),               # Convert to tensor
        #transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),  # Normalize
    ])
    
    # Apply transforms to image and annotation
    image = transform(image)
    #annotation = transform(annotation)
    
    return image, annotation

# Example usage
image_path = "/Users/jc/Downloads/dp_gan/18_200235_220616_01.jpg"
annotation_path = "/Users/jc/Downloads/dp_gan/mask_18_200235_220616_01.jpg"
output_size = (512, 512)  # Output size for cropped regions

image, annotation = preprocess(image_path, annotation_path, output_size)

to_pil = transforms.ToPILImage()
image = to_pil(image)
plt.imshow(image)
plt.axis('off')
plt.show()