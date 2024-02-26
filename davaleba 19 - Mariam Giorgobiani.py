#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Node: #Single Node in a Linked List
    def __init__(self, data): #Initializes node with a given data
        self.data = data
        self.next = None  #Initially there is no next node


class LinkedList:
    def __init__(self):
        self.head = None  #Initially it is not defined

    def append(self, data):  #Add new node
        new_node = Node(data)

        if self.head is None: #If the linked list is empty, the new node becomes the first node
            self.head = new_node
            return

        last_node = self.head  #last node becomes head

        while last_node.next: #If there is another node after last_node, last_node is updated to the next node
            last_node = last_node.next

        last_node.next = new_node

    def insert(self, data, index):   #Insert a new node with a given data and a specific index
        new_node = Node(data)

        if index == 0:    #If it is the first record, this will be initialized as head
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head   
        current_index = 0

        while current_node.next and current_index < index - 1:  #Current_node is updated to the next node by assigning current_node.next to current_node
            current_node = current_node.next
            current_index += 1

        new_node.next = current_node.next
        current_node.next = new_node

    def remove(self, data):   #Remove specific data from Linked List

        if self.head is None:
            return

        if self.head.data == data:  #Move the head to the next node
            self.head = self.head.next
            return

        current_node = self.head

        while current_node.next and current_node.next.data != data:  #Update next pointer to skip the node that was removed
            current_node = current_node.next

        if current_node.next:
            current_node.next = current_node.next.next

    def display_info(self):
        current_node = self.head

        while current_node is not None:  #Printing the data of each node followed by the arrows until current_node becomes None
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print()


linked_list = LinkedList()
linked_list.append(10)
linked_list.append(2)
linked_list.append(5)
linked_list.append(4)
linked_list.append(4)
linked_list.append(4)
linked_list.append(11)
linked_list.append(25)
linked_list.display_info()
linked_list.insert("Mariami", 3)
linked_list.insert(11, 5)
linked_list.display_info()
linked_list.remove("Mariami")
linked_list.remove(4)
linked_list.display_info()


# In[ ]:




