import json
import matplotlib.pyplot as plt 
from matplotlib.patches import Polygon
import numpy as np 
from skimage.draw import polygon as draw_polygon
import os 


def load_annotations(json_file):
    with open (json_file, 'r') as f:
        return json.load(f)
    
json_file = '/Users/jc/Downloads/18_200235_220616_01.json'    
annotations = load_annotations(json_file)

mask_folder = './mask'
if not os.path.exists(mask_folder):
    os.mkdir(mask_folder)

#define colors
colors = {
        'background': (0, 0, 0), #0 background +
        'vehicle': (255, 90, 241), #1 vehicle +
        'bus': (139, 145, 58), #2 bus +
        'truck': (190, 235, 159), #3 truck + 
        'policeCar': (153, 40, 184), #4 policeCar + 
        'ambulance': (255, 255, 255), #5 ambulance +
        'schoolBus': (248, 181, 0), #6 schoolBus +
        'otherCar': (0, 243, 64), #7 otherCar  +
        'motorCycle': (173, 128, 36), #8 motorCycle +
        'bicycle': (0, 0, 0), #9 bicycle
        'twoWeeler': (0, 0, 0), #10 twoWeeler
        'pedestrian': (0, 117, 255), #11 pedestrian  +
        'rider': (36, 98, 136), #12 rider + 
        'freespace': (100, 30, 255), #13 freespace   +
        'curb': (255, 72, 127), #14 curb       +
        'sidewalk': (0, 0, 0), #15 sidewalk
        'crossWalk': (0, 0, 0), #16 crossWalk
        'safetyZone': (0, 207, 255), #17 safetyZone  +
        'roadMark': (248, 28, 81), #18 roadMark    +
        'whiteLane': (255, 188, 123), #19 whileLane  +
        'yellowLane': (255, 127, 36), #20 yellowLane  + 
        'blueline': (152, 255, 141), #21 blueline   +
        'redLine': (0, 0, 24), #22 redLine
        'stopLane': (255, 188, 123), #23 stopLane
        'trafficSign': (253, 255, 186), #24 trafficSign +
        'trafficLight': (0, 223, 197), #25 trafficLight + 
        'constructionGuide': (0, 0, 0), #26 constructionGuide
        'trafficDrum': (42, 13 ,107), #27 trafficDrum   +
        'rubberCone': (2, 166, 118), #28 rubberCone
        'warningTriangle': (0, 0, 0), #29 warningTriangle + 
        'fense': (200, 219, 31), #30 fence     + 
        'unknow': (0, 0, 0), # 31 Unknow
    }

class_labels = []
polygons = []

file_name = annotations['information']['filename']
file_res = annotations['information']['resolution']
print(file_name)
print(os.path.splitext(file_name))
print(os.path.splitext(file_name)[0])

print(file_res)

#create a blank mask 
mask_image = np.zeros((file_res[1], file_res[0], 3), dtype=np.uint8)


for annotation in annotations['annotations']:
    class_label = annotation['class']
    print(class_label)
    polygon = annotation['polygon']

    class_labels.append(class_label)
    polygons.append(polygon)

#create a new figure and axis
fig, ax = plt.subplots()

for class_label, polygon in zip(class_labels, polygons):
    # Convert the flat list of coordinates to pairs of (x, y)
    polygon_pairs = np.array([(polygon[i], polygon[i+1]) for i in range(0, len(polygon), 2)])
    
    color = colors.get(class_label, [128, 0, 0])

    rr, cc = draw_polygon(polygon_pairs[:, 1], polygon_pairs[:, 0], mask_image.shape[:2])
    mask_image[rr, cc] = color

plt.imshow(mask_image)
#turn off axis
plt.axis('off')

#show or save 
#plt.show()
plt.imsave(os.path.join(mask_folder, f"{file_name}"), mask_image)


