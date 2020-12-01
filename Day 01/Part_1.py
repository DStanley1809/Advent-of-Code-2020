# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 13:42:24 2020

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
    
    # Generate a list of all possible combinations of two numbers from the list
    pairs = list(itertools.combinations(inputList, 2))
    
    # Iterate over the list of pairs to find the pair that adds up to 2020
    for i in pairs:
        if i[0] + i[1] == 2020:
            # Return the product of the pair
            return i[0]*i[1]
        
print(reportRepair())