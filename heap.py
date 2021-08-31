#Implementation of a generic binary heap in python, it is important that all
#functions are written for the operation of the heap. Everything that must
#be written is described in the functions and constructors!
#obs: All functions without comments do not need to be modified unless you know what you are doing

import scipy

class Node:
    def __init__(self, value:int):
        # Node constructor, holds the information of what will be stored in the heap
        self.value = value
    
    def __eq__(self, B):  
        # Equal comparison function, how to know if two Nodes are equal?
        return self.value == B.value
    def __str__(self):
        # How should we print Node?
        #The return is a string ex: return str(value)
        return str(self.value)

class Heap:
    def __init__(self):
        self.heap = [Node(-1)]*5
        self.current_size = 0

    #def __init__(self):
        # Heap constructor, here we must define an array self.heap followed by a variable that holds
        # the number of items that exist in the heap both must be named: heap and current_size.
        # You are free to create your own constructor but remember that at the end of the constructor
        # the heap must contain both elements self.heap and self.current_size to work!

    def priority_function(self, A:Node, B:Node): 
        # Priority function, it should simply return true if element A needs to be replaced
        # by element B, i.e. element B has higher priority than element A.
        return A.value > B.value # Max heap

    #def update(self):
        # Here you are free to update a specific node in your heap
    
    def set_max_priority(self, i:int): 
        # Which value gives a node the highest priority?
        self.heap[i] = 999

    def has_left_child(self, i:int):
        return (2*i + 1) < self.current_size
    
    def has_right_child(self, i:int):
        return (2*i + 2) < self.current_size
    
    def has_parent(self, i:int):
        return ((i-1)//2) > -1
    
    def get_left_child_index(self, i:int):
        return (2*i + 1)
    
    def get_right_child_index(self, i:int):
        return (2*i + 2)
    
    def get_parent_index(self, i:int):
        return (i-1)//2
    
    def get_left_child(self, i:int):
        return self.heap[2*i + 1]
    
    def get_right_child(self, i:int):
        return self.heap[2*i + 2]
    
    def get_parent(self, i:int):
        return self.heap[(i-1)/2]
    
    def swap(self, x, y):
        temp = self.heap[x]
        self.heap[x] = self.heap[y]
        self.heap[y] = temp

    def heapfy_down(self, i:int):
        current_index = i
        done = False

        while not done:
            done = True
            if self.has_left_child(current_index) and self.has_right_child(current_index):
                if self.priority_function(self.get_left_child(current_index), self.get_right_child(current_index)):
                    if self.priority_function(self.get_left_child(current_index), self.heap[current_index]):

                        self.swap(current_index, self.get_left_child_index(current_index))
                        current_index = self.get_left_child_index(current_index)
                        done = False
                
                else:
                    if self.priority_function(self.get_right_child(current_index), self.heap[current_index]):

                        self.swap(current_index, self.get_right_child_index(current_index))
                        current_index = self.get_right_child_index(current_index)
                        done = False
                    
            else:
                if self.has_left_child(current_index):
                    if self.priority_function(self.get_left_child(current_index), self.heap[current_index]):

                        self.swap(current_index, self.get_left_child_index(current_index))
                        current_index = self.get_left_child_index(current_index)
                        done = False
                    
                if self.has_right_child(current_index) and done:
                    if self.priority_function(self.get_right_child(current_index), self.heap[current_index]):

                        self.swap(current_index, self.get_right_child_index(current_index))
                        current_index = self.get_right_child_index(current_index)
                        done = False
                    
    def bubbleup(self, i:int):
        current_index = i
        done = False

        while not done:
            done = True
            if self.has_parent(current_index):
                if self.priority_function(self.heap[current_index], self.heap[self.get_parent_index(current_index)]):

                    self.swap(current_index, self.get_parent_index(current_index))
                    current_index = self.get_parent_index(current_index)
                    done = False
    
    def build_offline(self):
        i = len(self.heap) - 1
        while i > -1:
            self.heapfy_down(i)
            i -= 1

    def insert(self, n:Node):
        self.heap[self.current_size] = n
        self.bubbleup(self.current_size)
        self.current_size += 1
     
    def print_heap(self):
        for i in range(0, self.current_size):
            print(self.heap[i])
    
    def pop(self):
        temp = self.heap[0]
        if self.current_size:
            self.swap(0, self.current_size - 1)
            self.current_size -= 1
            self.heapfy_down(0)
            return temp
        else:
            print("Empty heap and a pop occurred!")
            return -1
        
    def top(self):
        return self.heap[0]
