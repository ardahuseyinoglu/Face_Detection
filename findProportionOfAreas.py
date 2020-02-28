def findProp(x,y,w,h,ax,ay,aw,ah):
    x1 = x
    y1 = -y-h
    x2 = x+w
    y2 = -y
    x3 = ax
    y3 = -ay-ah
    x4 = ax+aw
    y4 = -ay

    intersection_area = None
    
    x5 = max(x1, x3)
    y5 = max(y1, y3)
    
    x6 = min(x2, x4)
    y6 = min(y2, y4)
    
    x7 = x5
    y7 = y6

    x8 = x6
    y8 = y5

    if (x5 > x6 or y5 > y6) :
        intersection_area = 0
    else:
        height_of_intersection = y7-y5
        width_of_intersection = x8-x5
        intersection_area = height_of_intersection*width_of_intersection

    area_w_h = w*h
    area_aw_ah = aw*ah
    average_area = (area_w_h+area_aw_ah)/2

    return (intersection_area/average_area)



