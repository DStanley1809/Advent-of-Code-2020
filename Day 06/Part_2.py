# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 14:18:51 2020

@author: David Stanley
"""

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
    for group in forms:
        # Create dictionary with 26 entries (keys a-z). Values initialised to 0
        responseDict = {}
        alphaString = string.ascii_lowercase        
        for c in alphaString:
            responseDict[c] = 0
        
        # Count how many respondees present in group
        respondeeCount = len(group)
        
        # Iterate over each form within the group:
        for form in group:            
            # Iterate over answers in form
            for a in form:
                # Ignore newline characters
                if a != "\n":
                    responseDict[a] += 1
        
        # Iterate over dictionary, if value for each letter key matches number
        # of respondees, incrememnt yes count by one to show that every
        # respondee answered that question with yes
        for key in responseDict:
            if responseDict.get(key) == respondeeCount:
                yesCount += 1
    
    #Return total yes count                
    return yesCount
        
print(customCustoms())

    