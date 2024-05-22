import os
import numpy as np
from PIL import Image
from multiprocessing import Pool 
from tqdm import tqdm

def colorIds_to_instanceIds(filename):
    #print(f"{filename}")
    input_path = os.path.join(colorIds_folder, filename)
    print(f"{input_path}")
    output_path = os.path.join(instanceIds_folder, filename.replace('.png', '_instanceIds.png'))
    print("ColorIds Folder:", colorIds_folder)
    print("InstanceIds Folder:", instanceIds_folder)
   
    
    # Load color mapping
    color_mapping = {}
    with open("aihub_color.txt", "r") as f:
        for line in f:
            r, g, b, label= line.strip().split()
            color_mapping[(int(r), int(g), int(b))] = str(label)
        print("Color Mapping:", color_mapping)
    # Load segmentation mask image

    mask_image = np.array(Image.open(input_path))


    # Map colors to class IDs
    class_ids = np.zeros_like(mask_image, dtype=np.uint8)
    for color, label in color_mapping.items():
        class_ids[np.all(mask_image == np.array(color), axis=-1)] = label

    # Generate instance IDs
    unique_labels = np.unique(class_ids)
    instance_ids = {label: i for i, label in enumerate(unique_labels)}

    # Replace colors with instance IDs
    instance_mask = np.zeros_like(class_ids, dtype=np.uint8)
    for label, instance_id in instance_ids.items():
        instance_mask[class_ids == label] = instance_id

    # Save or use the instance segmentation mask
    instance_mask_image = Image.fromarray(instance_mask)
    instance_mask_image.save(output_path)
    print("Processed:", filename)

def colorIds_to_instanceIds_wrapper(colorId_files):
    
    for colorId_file in colorId_files:
        
        colorIds_to_instanceIds(colorId_file)



if __name__ == "__main__":

    colorIds_folder = '/Users/jc/Downloads/aihub_dataset_1840_add_class/colorIds'    

    instanceIds_folder = '/Users/jc/Downloads/aihub_dataset_1840_add_class/instanceIds'
    # print("ColorIds Folder:", colorIds_folder)
    # print("InstanceIds Folder:", instanceIds_folder)
    if not os.path.exists(instanceIds_folder):
        os.mkdir(instanceIds_folder)
    
    colorId_files_list = os.listdir(colorIds_folder)
    #print(len(colorId_files_list))
    chunk_size = len(colorId_files_list) // 10
    
    colorId_chunks = [colorId_files_list[i:i+chunk_size] for i in range(0, len(colorId_files_list), chunk_size)]
    #print(colorId_chunks)

    results = []
    pbar = tqdm(total=10)
    pbar.set_description('Processing colorIds to instanceIds -> ')
    update = lambda *args: pbar.update()
    
    pool = Pool(10)
    
    for chunk in colorId_chunks:
        #print(chunk)
        pool.apply_async(colorIds_to_instanceIds_wrapper, (chunk,), callback=update)

    pool.close()
    pool.join()
            
      
    print('Done')