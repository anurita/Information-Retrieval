# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 13:07:36 2017

@author: anu
"""
import collections
import numpy as np

def computation(M, matrix_b, damp_factor, v):
    return np.matrix(damp_factor * M * v + matrix_b)

def initialize(length, damp_factor):
    matrix_b = np.matrix((1.0/length) * np.ones((length, 1)))
    matrix_b = (1-damp_factor)*matrix_b
    v = np.matrix((1.0/length) * np.ones((length, 1)))
    return(matrix_b, v)

def compute_pagerank(M, matrix_b, damp_factor, v):
        no_of_iterations = 1
        modified_rank = computation(M, matrix_b, damp_factor, v)
        while not (sum(abs(modified_rank-v))) <= 0.001:
            v = modified_rank
            modified_rank = computation(M, matrix_b, damp_factor, v)
            no_of_iterations = no_of_iterations + 1
        return(no_of_iterations, v)
        
#declarations
nodes = {}
damp_factor = 0.85

# read txt file and form dictionary
f = input("Enter full path to the graph text file (use space as delimiter for i j k): ")
with open(f, 'r') as file:
    for line in file:
        i, j, k = line.split(" ")
        if i in nodes:
            nodes.get(i).append(j)
            if j not in nodes:
                nodes[j] = []
        else:
            nodes[i] = []
            nodes[i].append(j)
            if j not in nodes:
                nodes[j] = []

ordered_nodes = collections.OrderedDict(sorted(nodes.items()))
length = len(nodes)
M = np.zeros((length, length))
for row in range(0, length):
    src = list(ordered_nodes.keys())[row]
    outlinks = ordered_nodes[str(src)]
    for col in range(0, length):
        dest = list(ordered_nodes.keys())[col]
        if str(dest) in outlinks:
            M[row][col] = 1.0/float(len(outlinks))
            
M = np.matrix(M.transpose())
matrix_b, v = initialize(length, damp_factor)
print("Original matrix M\n" , M)
print("Original rank vector r\n", v)
total_iterations, R = compute_pagerank(M, matrix_b, damp_factor, v)
print("Converged matrix R \n " , R)
print("Total iterations = " , total_iterations)


        
            
        
            
           
        