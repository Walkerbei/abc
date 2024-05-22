city_color_class = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (111, 74, 0), (81, 0, 81),
                         (128, 64, 128), (244, 35, 232), (250, 170, 160), (230, 150, 140), (70, 70, 70), (102, 102, 156), (190, 153, 153),
                         (180, 165, 180), (150, 100, 100), (150, 120, 90), (153, 153, 153), (153, 153, 153), (250, 170, 30), (220, 220, 0),
                         (107, 142, 35), (152, 251, 152), (70, 130, 180), (220, 20, 60), (255, 0, 0), (0, 0, 142), (0, 0, 70),
                         (0, 60, 100), (0, 0, 90), (0, 0, 110), (0, 80, 100), (0, 0, 230), (119, 11, 32), (0, 0, 142)],

morai2cityscapes_color_class = [(0, 0, 142), #0 vehicle -> 26
                    (0 , 60, 100 ), #1 bus -> 28
                    (0, 0, 70), #2 truck
                    (0, 0, 142), #3 policecar
                    (0, 0, 90), #4 ambulance
                    (0, 0, 110), #5 schoolbus
                    (0, 80, 100), #6 othercar
                    (0, 0, 230), #7 motorcycle
                    (119, 11, 32), #8 bicycle
                    (119, 11, 32), #9 twoWheeler
                    (220, 20, 60), #10 pedestrian
                    (255, 0, 0), #11 rider
                    (128, 64, 128), #12 freespace
                    (250, 170, 160), #13 curb
                    (244, 35, 232), #14 sidewalk
                    (128, 64, 128), #15 crosswalk
                    (128, 64, 128), #16 safetyZone
                    (128, 64, 128), #17 speedbump
                    (128, 64, 128), #18 roadMark
                    (128, 64, 128), #19 whileLane
                    (128, 64, 128), #20 yellowLane
                    (128, 64, 128), #21 blueline
                    (128, 64, 128), #22 redLine
                    (128, 64, 128), #23 stopLane
                    (220, 220, 0), #24 trafficsign
                    (250, 170, 30), #25 trafficlight
                    (70, 70, 70), #26 constructionGuide
                    (102, 102 ,156), #27 trafficDrum
                    (70, 70, 70), #28 rubberCone
                    (70, 70, 70), #29 warningTriangle
                    (102, 102 ,156), #30 fence
                    (0, 0, 0), #31 egoVehicle
                    (0, 0, 0) #32 backround
                    ]

morai_color_class = [(255, 90, 241), #0 vehicle 
                    (66 , 7, 158 ), #1 bus
                    (0, 243, 64), #2 truck
                    (248, 158, 235), #3 policecar
                    (211, 222, 241), #4 ambulance
                    (255, 0, 0), #5 schoolbus
                    (200, 30, 141), #6 othercar
                    (255, 255, 153), #7 motorcycle
                    (248, 171, 255), #8 bicycle
                    (0, 182, 182), #9 twoWheeler
                    (255, 0, 233), #10 pedestrian
                    (100, 30, 255), #11 rider
                    (9, 161, 181), #12 freespace
                    (80, 180, 98), #13 curb
                    (118, 78, 176), #14 sidewalk
                    (255, 141, 181), #15 crosswalk
                    (0, 207, 255), #16 safetyZone
                    (134, 59, 141), #17 speedbump
                    (248, 28, 81), #18 roadMark
                    (255, 188, 123), #19 whileLane
                    (255, 100, 0), #20 yellowLane
                    (152, 255, 141), #21 blueline
                    (123, 165, 24), #22 redLine
                    (106, 163, 145), #23 stopLane
                    (241, 90, 41), #24 trafficsign
                    (0, 233, 197), #25 trafficlight
                    (254, 209, 69), #26 constructionGuide
                    (50, 230 ,155), #27 trafficDrum
                    (136, 153, 179), #28 rubberCone
                    (153, 0, 76), #29 warningTriangle
                    (247, 234, 110), #30 fence
                    (0, 182, 255), #31 egoVehicle
                    (210, 229, 168) #32 backround
                    ]

                   

aihub_color_class = [(0, 0, 0), #0 background +
                    (255 , 90, 241 ), #1 vehicle +
                    (0, 243, 64), #2 bus
                    (190, 235, 159), #3 truck + 
                    (211, 222, 241), #4 policeCar
                    (255, 0, 0), #5 ambulance
                    (200, 30, 141), #6 schoolBus
                    (255, 255, 153), #7 otherCar
                    (248, 171, 255), #8 motorCycle
                    (0, 182, 182), #9 bicycle
                    (255, 0, 233), #10 twoWeeler
                    (100, 30, 255), #11 pedestrian
                    (9, 161, 181), #12 rider
                    (100, 30, 255), #13 freespace   +
                    (255, 188, 123), #14 curb       ？
                    (255, 141, 181), #15 sidewalk
                    (0, 207, 255), #16 crossWalk
                    (0, 207, 255), #17 safetyZone  +
                    (248, 28, 81), #18 roadMark    +
                    (255, 188, 123), #19 whileLane  +
                    (255, 100, 0), #20 yellowLane
                    (152, 255, 141), #21 blueline
                    (123, 165, 24), #22 redLine
                    (106, 163, 145), #23 stopLane
                    (253, 255, 186), #24 trafficsign +
                    (0, 233, 197), #25 trafficlight
                    (254, 209, 69), #26 constructionGuide
                    (42, 13 ,107), #27 trafficDrum   +
                    (136, 153, 179), #28 rubberCone
                    (153, 0, 76), #29 warningTriangle
                    (200, 219, 31), #30 fence    +
                    ]