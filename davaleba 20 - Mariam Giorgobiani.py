#!/usr/bin/env python
# coding: utf-8

# In[2]:


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_leaf_nodes(node):
    if node is None:
        return
    
    if node.left is None and node.right is None:
        print(node.value)
        return
    
    print_leaf_nodes(node.left)
    print_leaf_nodes(node.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Leaf nodes of the tree:")
print_leaf_nodes(root)


# In[4]:


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def count_edges(root):
    if root is None:
        return 0
    return count_nodes(root) - 1

def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Total edges in the binary tree:", count_edges(root))


# In[ ]:




