from aihub_labelmap_v2 import aihub_cmap_31, aihub_cmap_34
import numpy as np
import json
import ast
#######################################
# cmap1 = []

# def rgb_to_hex(rgb):
#     """Convert RGB tuple to hexadecimal color code."""
#     return '#{:02x}{:02x}{:02x}'.format(*rgb)

# my_list = []
# file_name = '/Users/jc/Downloads/usefulScripts2024/aihub_colormap_v3_xlabel.json'


# file1=open(file_name, 'a')
# file1.write('[')
# #print(len(aihub_cmap_31))
# for i in range(len(aihub_cmap_31)):
#     #cmap1.append(aihub_cmap_31[i].color)
#     print(aihub_cmap_31[i].color[0], aihub_cmap_31[i].color[1], aihub_cmap_31[i].color[2], aihub_cmap_31[i].name)
#     rgb_color = (aihub_cmap_31[i].color[0], aihub_cmap_31[i].color[1], aihub_cmap_31[i].color[2])
#     hex_color = rgb_to_hex(rgb_color)
#     #print("Hexadecimal color:", hex_color)
#     #print(type(hex_color))

#     my_dict = {"type": "rgb", "colors":{}}
#     # for j in (aihub_cmap_31[i].name):
#     #     print(j)

#     # my_dict2 = {"f'aihub_cmap_31[i].name'": [aihub_cmap_31[i].color[0], aihub_cmap_31[i].color[1], aihub_cmap_31[i].color[2]]}
#     # print(my_dict2)
#     json_str= json.dumps(my_dict, ensure_ascii=False)
#     #print(json_str)
    

    
#     #file1.writelines(f'{json_str}\n')
# file1.write(']')
# file1.close()


# # with open(file_name, "r") as f:
# #     content = [line.strip() for line in f.readlines()]

# # with open(file_name, "w") as f:
# #     f.write(",\n".join(content)+",")



# #print(cmap1)
# #cmap_arr1 = np.array(cmap1, dtype=np.uint8)
# # print(cmap_arr)
#######################################################
from aihub_labelmap_v2 import aihub_cmap_34
import json


# colors_dict = {"type": "rgb", "colors": {}}

# for i in aihub_cmap_34:
#     colors_dict["colors"][i.name] = [i.color[0], i.color[1] ,i.color[2]]
# print(colors_dict)
color_map = []


for i in range(len(aihub_cmap_34)):
    #print(aihub_cmap_34[0])
    #for j in range(len(i))
    colors_dict2 = {}
    colors_dict2["name"] = aihub_cmap_34[i].name
    colors_dict2["id"] = aihub_cmap_34[i].id
    colors_dict2["color"] = [aihub_cmap_34[i].color[0], aihub_cmap_34[i].color[1] , aihub_cmap_34[i].color[2]] 
    color_map.append(colors_dict2)
print(color_map)
# for dict_entry in color_map:
#     print(dict_entry)

# print(len(color_map))
# print(color_map[0])


# # Write the dictionary to a JSON file
# file_name = '/Users/jc/Downloads/usefulScripts2024/aihub_colormap_v4_xlabel.json'
# with open(file_name, 'w') as file1:
#     json.dump(colors_dict, file1, indent=4)

