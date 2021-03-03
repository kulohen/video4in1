# -*- coding:utf-8 -*-
import re
import os
import time



open_dic = "C:/Users/29125/PycharmProjects/video4in1"
print(open_dic)
print(os.path.exists(open_dic))

file_1 = "C:/Users/29125/PycharmProjects/video4in1/【sexinsex.net】抬杠大队呢.mp4"

dir,file = os.path.split(file_1)
print(dir, file)

print(os.path.join(dir, '4in1_'+file))