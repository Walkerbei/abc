
#!/usr/bin/python
#
# aihub labels
#

from __future__ import print_function, absolute_import, division
from collections import namedtuple
import numpy as np

##Debug log 
### C240425 label1/2 ->aihub_cmap_31, aihub_cmap_34
#--------------------------------------------------------------------------------
# Definitions
#--------------------------------------------------------------------------------

#a label and all meta information
Label = namedtuple( 'Label' , [

    'name'        , # The identifier of this label, e.g. 'car', 'person', ... .
                    # We use them to uniquely name a class

    'id'          , # An integer ID that is associated with this label.
                    # The IDs are used to represent the label in ground truth images
                    # An ID of -1 means that this label does not have an ID and thus
                    # is ignored when creating ground truth images (e.g. license plate).
                    # Do not modify these IDs, since exactly these IDs are expected by the
                    # evaluation server.

    'category'    , # The name of the category that this label belongs to


    'color'       , # The color of this label
    ] )



aihub_cmap_31 = [
    #       name                     id       category                       color
    Label(  'background'           ,  0 ,      'void'                , (0,   0,   0)   ),
    Label(  'vehicle'              ,  1 ,      'vehicle'             , (255, 90, 241)  ),
    Label(  'bus'                  ,  2 ,      'vehicle'             , (139, 145, 58)  ),
    Label(  'truck'                ,  3 ,      'vehicle'             , (190, 235, 159) ),
    Label(  'policeCar'            ,  4 ,      'vehicle'             , (153, 40, 184)  ),
    Label(  'ambulance'            ,  5 ,      'vehicle'             , (255, 255, 255) ),
    Label(  'schoolBus'            ,  6 ,      'vehicle'             , (248, 181, 0)   ),
    Label(  'otherCar'             ,  7 ,      'vehicle'             , (0, 243, 64)    ),
    Label(  'motorCycle'           ,  8 ,      'vehicle'             , (173, 128, 36)  ),
    Label(  'bicycle'              ,  9 ,      'vehicle'             , (0,   0,   0)   ),
    Label(  'twoWheeler'            , 10 ,      'vehicle'             , (0,   0,   0)   ),
    Label(  'pedestrian'           , 11 ,      'human'               , (0, 117, 255)   ),
    Label(  'rider'                , 12 ,      'human'               , (36, 98, 136)   ),
    Label(  'freespace'            , 13 ,      'flat'                , (100, 30, 255)  ),
    Label(  'curb'                 , 14 ,      'construction'        , (255, 72, 127)  ),
    Label(  'sidewalk'             , 15 ,      'flat'                , (0,   0,   0)   ),
    Label(  'crosswalk'            , 16 ,      'flat'                , (0,   0,   0)   ),
    Label(  'safetyZone'           , 17 ,      'flat'                , (0, 207, 255)   ),
    Label(  'roadMark'             , 18 ,      'flat'                , (248, 28, 81)   ),
    Label(  'whiteLane'            , 19 ,      'flat'                , (255, 188, 123) ),
    Label(  'yellowLane'           , 20 ,      'flat'                , (255, 127, 36)  ),
    Label(  'blueLane'             , 21 ,      'flat'                , (152, 255, 141) ),
    Label(  'redLane'              , 22 ,      'flat'                , (0,   0,   24)  ),
    Label(  'stopLane'             , 23 ,      'flat'                , (255, 188, 123) ),
    Label(  'trafficSign'          , 24 ,      'object'              , (253, 255, 186) ),
    Label(  'trafficLight'         , 25 ,      'object'              , (0, 223, 197)   ),
    Label(  'constructionGuide'    , 26 ,      'construction'        , (0,   0,   0)   ),
    Label(  'trafficDrum'          , 27 ,      'object'              , (42, 13 ,107)   ),
    Label(  'rubberCone'           , 28 ,      'object'              , (2, 166, 118)   ),
    Label(  'warningTriangle'      , 29 ,      'object'              , (0,   0,   0)   ),
    Label(  'fence'                , 30 ,      'object'              , (200, 219, 31)  ),
    Label(  'unknown'               , 31 ,      'void'                , (0,   0,   0)   ),
]

aihub_cmap_34 = [
    #       name                     id       category                       color
    Label(  'background'           ,  0 ,      'void'                , (0,   0,   0)   ),
    Label(  'vehicle'              ,  1 ,      'vehicle'             , (255, 90, 241)  ),
    Label(  'bus'                  ,  2 ,      'vehicle'             , (139, 145, 58)  ),
    Label(  'truck'                ,  3 ,      'vehicle'             , (190, 235, 159) ),
    Label(  'policeCar'            ,  4 ,      'vehicle'             , (153, 40, 184)  ),
    Label(  'ambulance'            ,  5 ,      'vehicle'             , (255, 255, 255) ),
    Label(  'schoolBus'            ,  6 ,      'vehicle'             , (248, 181, 0)   ),
    Label(  'otherCar'             ,  7 ,      'vehicle'             , (0, 243, 64)    ),
    Label(  'motorCycle'           ,  8 ,      'vehicle'             , (173, 128, 36)  ),
    Label(  'bicycle'              ,  9 ,      'vehicle'             , (0,   0,   0)   ),
    Label(  'twoWheeler'            , 10 ,      'vehicle'             , (0,   0,   0)   ),
    Label(  'pedestrian'           , 11 ,      'human'               , (0, 117, 255)   ),
    Label(  'rider'                , 12 ,      'human'               , (36, 98, 136)   ),
    Label(  'freespace'            , 13 ,      'flat'                , (100, 30, 255)  ),
    Label(  'curb'                 , 14 ,      'construction'        , (255, 72, 127)  ),
    Label(  'sidewalk'             , 15 ,      'flat'                , (0,   0,   0)   ),
    Label(  'crosswalk'            , 16 ,      'flat'                , (0,   0,   0)   ),
    Label(  'safetyZone'           , 17 ,      'flat'                , (0, 207, 255)   ),
    Label(  'roadMark'             , 18 ,      'flat'                , (248, 28, 81)   ),
    Label(  'whiteLane'            , 19 ,      'flat'                , (255, 188, 123) ),
    Label(  'yellowLane'           , 20 ,      'flat'                , (255, 127, 36)  ),
    Label(  'blueLane'             , 21 ,      'flat'                , (152, 255, 141) ),
    Label(  'redLane'              , 22 ,      'flat'                , (0,   0,   24)  ),
    Label(  'stopLane'             , 23 ,      'flat'                , (255, 188, 123) ),
    Label(  'trafficSign'          , 24 ,      'object'              , (253, 255, 186) ),
    Label(  'trafficLight'         , 25 ,      'object'              , (0, 223, 197)   ),
    Label(  'constructionGuide'    , 26 ,      'construction'        , (0,   0,   0)   ),
    Label(  'trafficDrum'          , 27 ,      'object'              , (42, 13 ,107)   ),
    Label(  'rubberCone'           , 28 ,      'object'              , (2, 166, 118)   ),
    Label(  'warningTriangle'      , 29 ,      'object'              , (0,   0,   0)   ),
    Label(  'fence'                , 30 ,      'object'              , (200, 219, 31)  ),
    Label(  'unknown'               , 31 ,      'void'                , (0,   0,   0)  ),
    Label(  'pole'                 , 32 ,      'object'              , (153, 153, 153) ),     #cityscapes color
    Label(  'wall'                 , 33 ,      'construction'        , (102, 102, 156)   ),
    Label(  'crack'                , 34 ,      'void'                , (0,   0,   142)   ),
]


#-------------------------------------------------------------------------#
# instance to use 
#from aihub_labelmap_v2 import aihub_cmap_31, aihub_cmap_34

# cmap = []
# print(len(aihub_cmap_31))
# for i in range(len(aihub_cmap_31)):
#     cmap.append(aihub_cmap_31[i].color)
# print(cmap)

####if np.array format is need 
# cmap_arr = np.array(cmap, dtype=np.uint8)
# # print(cmap_arr)
# # print(type(cmap_arr))
 #-------------------------------------------------------------------------#   

