#!/usr/bin/env python
# coding: utf-8

# In[3]:


def decorator(func):
    def wrapper(x):
        if x >= 0:
            return func(x)
        else:
            raise ValueError("It is not non-negative number")  
        
    return wrapper

@decorator
def num(x):
        return x
    
result = num(x=10)
print(result)


# In[2]:


class Functor:
    def __init__(self, func):
        self.func = func
        
    def __call__(self, x):
        if x >= 0:
            return x
        else:
            raise ValueError("It is not non-negative number")
                
def num(x):
    return x

my_func = Functor(num)
result = my_func(8)
result


# In[1]:


def decorator(func):
    def wrapper(balance, money):
        money += 1
        if balance >= money:
            return func(balance, money)
        else:
            raise ValueError("Not enough money")  
        
    return wrapper

@decorator
def transaction(balance, money):
        return balance - money
    
result = transaction(balance=2000, money=22)
print(result)


# In[ ]:




