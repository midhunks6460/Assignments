# -*- coding: utf-8 -*-
"""assn-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kmqJ0tEEeZfclcGj4l9UoE6ajaKOQnGo
"""

list=[18,"Data",False,3.14,0,1]
print(list)
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])
print(list[5])
print(list[-1])
list.append(2)
print(list)
a=[3,4,5]
list.extend(a)
print(list)
list.insert(10,6)
print(list)
del list[0]
print(list)
list.remove("Data")
print(list)