#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import ast
print("Enter - Money you have got,cost of the item")
list1=ast.literal_eval(input())
m=list1[0] #total money
c=list1[1] #cost per item
n=m//c #number of item
w=m//c #number of wrappers
e=r=0
count=n
while w>=3:
    r=w%3 #remaining item
    e=w//3 #extra item
    count+=e
    w=e+r
print("You can have ",count," choclates")

