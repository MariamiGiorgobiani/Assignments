#!/usr/bin/env python
# coding: utf-8

# In[14]:


import json
import threading
import time 

data = {
    "name": "Mariami Giorgobiani",
    "age": 26,
    "email": "mariami.giorgobiani@gmail.com",
    "address": {
        "street": "Guramishvili",
        "city": "Tbilisi",
    },
    "occupation": ["Business Ananlyst"]
}

file_path = "data.json"

with open(file_path, "w") as json_file:
    json.dump(data, json_file, indent=4)

print(f"JSON data has been written to {file_path}")



data1 = {
    "name": "Mariami Giorgobiani",
    "age": 30,
    "email": "mariami.giorgobiani1@gmail.com",
    "address": {
        "street": "Tchavtchavadze",
        "city": "Tbilisi",
    },
    "occupation": ["Financial Ananlyst"]
}


file_path = "data1.json"

with open(file_path, "w") as json_file:
    json.dump(data1, json_file, indent=4)

print(f"JSON data has been written to {file_path}")



data2 = {
    "name": "Mariami Giorgobiani",
    "age": 25,
    "email": "mariami.giorgobiani2@gmail.com",
    "address": {
        "street": "Tsereteli",
        "city": "Tbilisi",
    },
    "occupation": ["Lecturer"]
}

file_path = "data2.json"

with open(file_path, "w") as json_file:
    json.dump(data2, json_file, indent=4)

print(f"JSON data has been written to {file_path}")


# In[15]:


def data():
    name = "data.json"
    with open(name, "r") as json_file:
        data = json.load(json_file)
        print(name)
        print(data)
    time.sleep(2)
        
def data1():
    name = "data1.json"
    with open(name, "r") as json_file:
        data1 = json.load(json_file)
        print(name)
        print(data1)
    time.sleep(2)
        
def data2():
    name = "data2.json"
    with open("data2.json", "r") as json_file:
        data2 = json.load(json_file)
        print(name)
        print(data2)
    time.sleep(2)
        
threading.Thread(target = data).start()
threading.Thread(target = data1).start()
threading.Thread(target = data2).start()


# In[19]:


import threading
from queue import Queue
import time

def worker(task_queue, list_name):
    while True:
        task = task_queue.get()
        if task == None:
            break
            
        print(f"Name of list is {list_name}, the number is {task} and is even: {task % 2 == 0}")
        time.sleep(1)
        task_queue.task_done()
        

task_queue = Queue()
num_workers = 3
numbers = [1, 6, 234, 34, 5, 59, 60, 456, 767, 40]

thread1 = threading.Thread(target=worker, args=(task_queue, "Stream 1"))
thread2 = threading.Thread(target=worker, args=(task_queue, "Stream 2"))
thread3 = threading.Thread(target=worker, args=(task_queue, "Stream 3"))

thread1.start()
thread2.start()
thread3.start()

for number in numbers:
    task_queue.put(number)
    
task_queue.join()

print("All tasks are done")


# In[ ]:




