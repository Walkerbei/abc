import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import os 
from torchvision import transforms 


#image2 = '/backup/jc/datasets/1_aihub_rgbANDmask/mask/train/88_104515_221001_33.jpg'
image = '/Users/jc/Downloads/18_200235_220616_01.jpg'
#img2 = Image.open(image)
img2 = cv2.imread(image, cv2.IMREAD_COLOR)
#img2 = cv2.resize(img2, (4096, 4096), interpolation=cv2.INTER_AREA)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)


# Define the vertices of the polygon
#vertices = np.array([[1280, 600], [1280, 640], [1920, 830], [1920, 750]], dtype=np.int32)
#vertices = np.array([[594, 833],[634, 833], [634, 970], [594, 970]], dtype=np.int32) # crum
#vertices = np.array([[788, 888],[1088, 888], [1088, 1388], [788, 1388]], dtype=np.int32) #roadmark1
#vertices = np.array([[1320, 550],[1370, 620], [1270, 620]], dtype=np.int32) #roadmark1

# Reshape the vertices array to fit the required format for cv2.fillPoly()
#vertices = vertices.reshape((-1, 1, 2))

#vertices2 = np.array([[450, 1080],[450, 950], [880, 590], [880, 620]], dtype=np.int32) #crum
#vertices2 = np.array([[1388, 888],[1688, 888], [1688, 1388], [1388, 1388]], dtype=np.int32) #roadmark2
#vertices2 = vertices2.reshape((-1, 1, 2))
# Reshape the vertices array to fit the r
# equired format for cv2.fillPoly()



#pixel_color = (31, 219, 200) #fence 
#cv2.fillPoly(img2, [vertices], pixel_color)
#cv2.fillPoly(img2, [vertices2], pixel_color)
# 
#1img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

###################################


# input_img = 'design4444444.png'
# path  = '/Users/jc/Downloads/26_morai2aihub_test22/seg_1_color/'
# path_1 = os.path.join(path, input_img)
# img3 = np.array(Image.open(path_1))
# img3 = Image.fromarray(img3)
# print(img2.shape)
# img3.save('/Users/jc/Downloads/26_morai2aihub_test22/seg_1_color/design4444444.png')
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# for x in range(img2.width):
    
#     for y in range(img2.height):
#         pixel_color = img2.getpixel((x, y))[:3] # pixel color of seg image file
#         #print("x->",x, "y->", y , "pixel value->", pixel_color2)
        
        # for i in range(len(m2c_color_class)):
        #     if pixel_color2 == morai_color_class[i]:
                
        #         pixel_color2 =(m2c_color_class[i][0], m2c_color_class[i][1],m2c_color_class[i][2])  # by 1 or 0, 1 is for interested class
        #         img2.putpixel((x,y), pixel_color2)
        
        # if x >= 1500 and x < 1900:
        #     if y> 600 and y < 800:
        
        #         pixel_color = (31, 219, 200) #BGR
        #         cv2.rec



img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

#cv2.imwrite('43_HI_CO_T2W1_H1_E01_RE01_001_cv2resize_inter_area.png', img2)

img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
plt.imshow(img2)

plt.axis('off')  # Hide axes

plt.show()
# plt.imsave('HI_CO_T2W1_H1_E01_RE01_007_copy.png', img2)
