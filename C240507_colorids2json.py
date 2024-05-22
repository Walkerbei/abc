from PIL import Image
import os
import json
import shutil

#function to convert rgb tuple to hexadecimal color code
def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

#load colormap json file 
with open('/Users/jc/Downloads/usefulScripts2024/aihub_colormap_v3_xlabel.json', 'r') as f:
    colormap = json.load(f)
    #print(colormap)

def generate_annotation(mask_image_path, colormap, output_dir):
    #load the rgb mask image
    mask_image = Image.open(mask_image_path)

    #get pixel data from the mask image 
    pixels = mask_image.load()

    #initialize annotation dictionary
    annotations = {'annotations': []}
    # Iterate through each pixel in the image
    width, height = mask_image.size

    for y in range(height):
        for x in range(width):
            #get rgb color of the pixel 
            rgb = pixels[x, y]
            #print(rgb)
            #convert RGB tuple to hexadecimal color code 
            # hex_color = rgb_to_hex(rgb)
            # print(hex_color)

            #find label corresoponding to the color in the colormap 
            label = None 
            for key, value in colormap['colors'].items():
                if value == rgb:
                    label = key 
                    break 
            #if label exists, add annotation
            if label:
                annotations["annotations"].append({
                    "x": x,
                    "y": y,
                    "label": label
                })
   #output path 
    filename = os.path.basename(mask_image_path)
    output_path = os.path.join(output_dir, filename.replace(".png", ".json"))

    #write annotations to json file
    with open(output_path, 'w') as f:
        print(annotations)
        json.dump(annotations, f, indent=4)
    print(f"annotation file generated: {output_path}")

#Path to directory containing rgb mask jpg files 
mask_dir = "/Users/jc/Downloads/aihub_dataset_1840_add_class/Dataset2/ex1"

#directory to copy annotation json files
output_dir = "/Users/jc/Downloads/aihub_dataset_1840_add_class/Dataset2/ex1"

#loop through each jpg in the directory
for filename in os.listdir(mask_dir):
    if filename.endswith(".png"):
        mask_image_path =  os.path.join(mask_dir, filename)
        generate_annotation(mask_image_path, colormap, output_dir)




