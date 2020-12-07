# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 13:41:57 2020

@author: David Stanley
"""

import string

def customCustoms():
    
    # Read input text file and store contents
    inputText = open("input.txt", "r")
    inputContent = inputText.read()
    
    # Close opened file
    inputText.close()
    
    # Split input text in to a list of groups based on double new line 
    # characters
    groups = inputContent.split("\n\n")
    
    # Split each group in to idividual form responses based on single new line
    # characters
    forms = []
    
    for group in groups:
        forms.append(group.split("\n"))
        
    # Create counter to track number of questions answered with "Yes"
    # Initialise to 0
    yesCount = 0
    
    # Iterate over each group of forms
    for group in groups:
        # Create dictionary with 26 entries (keys a-z). Values initialised to 
        # no
        responseDict = {}
        alphaString = string.ascii_lowercase
        for c in alphaString:
            responseDict[c] = "no"
            
        # Iterate over answers in group
        for a in group:
            # Ignore newline characters
            if a != "\n":
                responseDict[a] = "yes"
                
        # Count number of yes values in response dictionary for this group and
        # add it to the total number of yes answers counted
        yesCount += sum(value == "yes" for value in responseDict.values())               
        
                    
    return yesCount
        
print(customCustoms())

    