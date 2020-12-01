# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 14:11:17 2020

@author: David Stanley
"""

import itertools

def reportRepair():
    
    # Read input text file and store contents
    inputText = open("input.txt", "r")
    inputContent= inputText.read()
    
    # Close opened file
    inputText.close()
    
    # Split input text in to a list based on line breaks then convert the 
    # strings to ints
    inputList = inputContent.split("\n")
    
    for i in range(0, len(inputList)):
        inputList[i] = int(inputList[i])
    
    # Generate a list of all possible combinations of three numbers from the list
    triples = list(itertools.combinations(inputList, 3))
    
    # Iterate over the list of triples to find the triple that adds up to 2020
    for i in triples:
        if i[0] + i[1] + i[2] == 2020:
            # Return the product of the triple
            return i[0]*i[1]*i[2]
        
print(reportRepair())