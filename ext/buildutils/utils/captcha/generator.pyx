# cython: language_level=3
import cv2
cimport numpy as np
import numpy as np
cdef int line_num = 10
cpdef tuple randcolor():        
    return (np.random.randint(0,255),np.random.randint(0,255),np.random.randint(0,255))
    
cpdef str randchar():
    return chr(np.random.randint(65,90))
    
cpdef tuple randpos(x_start,x_end,y_start,y_end):
    return (np.random.randint(x_start,x_end),
            np.random.randint(y_start,y_end))
    
    
cdef int img_heigth = 60
cdef int img_width = 240
cpdef dict generate(int pic_num):
    cdef dict imglist = {}
    cdef str img_name = ""
    cdef np.ndarray img
    cdef int x_pos 
    cdef int y_pos 
    cdef str char
    cdef bint success
    cdef np.ndarray encoded_img
    for i in range(pic_num):
        img_name = ""
        #生成一个随机矩阵，randint(low[, high, size, dtype])
        img = np.random.randint(100,200,(img_heigth,img_width, 3), np.uint8)
        #显示图像
        #cv2.imshow("ranImg",img)
        
        x_pos = 0
        y_pos = 25
        for i in range(4):
            char = randchar()
            img_name += char
            cv2.putText(img,char,
                        (np.random.randint(x_pos,x_pos + 50),np.random.randint(y_pos,y_pos + 35)), 
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.5,
                        randcolor(),
                        2,
                        cv2.LINE_AA)
            x_pos += 45
        
        #cv2.imshow("res",img)
        
        #添加线段
        for i in range(line_num):
            img = cv2.line(img,
                           randpos(0,img_width,0,img_heigth),
                           randpos(0,img_width,0,img_heigth),
                            randcolor(),
                            np.random.randint(1,2))
            
        
        success,encoded_img = cv2.imencode(".jpg",img)
        if success: imglist[img_name] = encoded_img.tobytes()
    return imglist
