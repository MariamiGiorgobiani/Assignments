#!/usr/bin/env python
# coding: utf-8

# In[35]:


import json

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Quantity: {self.quantity}")
        
        
    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }
        
product_1 = Product("Apple Smartphone", 1000, 10)
product_2 = Product("Samsung Smartphone", 700, 15)
product_3 = Product("Samsung TV", 2000, 5)

#product_1.display_info()

lst = [product_1, product_2, product_3]
print(lst)

product_dicts = [product.to_dict() for product in lst]

json_string = json.dumps(product_dicts, indent = 2)
print(type(json_string))
print(json_string)


with open("Json_data.json", "w") as json_file:
    json.dump(product_dicts, json_file)
    
with open("Json_data.json", "r") as json_file:
    python_data = json.load(json_file)
    
    for data in python_data:
        print(data)


# In[28]:





# In[ ]:




