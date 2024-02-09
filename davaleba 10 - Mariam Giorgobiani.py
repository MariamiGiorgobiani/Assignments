#!/usr/bin/env python
# coding: utf-8

# In[33]:


import random

def lin_search(list_for_search, value):
    
    for i in range(len(list_for_search)):
        if list_for_search[i] == value:
            return i
    return -1  

lst = [random.randint(-1000, 1000) for j in range(100)]
print(lst)
num = int(input(""))
result = lin_search(lst, num)
print(result)


# In[39]:


def selectionsort(list_for_sort):
    length = len(list_for_sort)
    
    for i in range(length):
        min_index = i
        
        for j in range(i+1, length):
            if list_for_sort[j] < list_for_sort[min_index]:
                min_index = j
        
        list_for_sort[i], list_for_sort[min_index] = list_for_sort[min_index], list_for_sort[i]
            
    
lst = [random.randint(-1000, 1000) for k in range(100)]
selectionsort(lst)
print(lst)

def bin_search(list_for_search, value):
    
    low = 0
    high = len(list_for_search) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if list_for_search[mid] < value:
            low = mid + 1
        elif list_for_search[mid] < value:
            high = mid - 1
        else: 
            return mid
    return -1

num = int(input(""))
result = bin_search(lst, num)
print(result)


# In[54]:


add_lambda = [i for i in range(0, 20) if (lambda a: a % 3 == 0)(i)]
print(add_lambda)


import random

def func(list_for_search, lmbd):
    
    for i in range(len(list_for_search)):
        for j in range(len(lmbd)):
            if list_for_search[i] == lmbd[j]:
                return i
    return -1  

lst = [random.randint(0, 20) for j in range(20)]
print(lst)
result = lin_search(lst, add_lambda)
print(result)


# In[ ]:




