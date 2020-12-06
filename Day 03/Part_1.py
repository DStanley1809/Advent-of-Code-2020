# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 18:39:43 2020

@author: David Stanley
"""

def tobogganTrajectory(moveX, moveY):
    
    # Read input text file and store contents
    inputText = open("input.txt", "r")
    inputContent = inputText.read()
    
    # Close opened file
    inputText.close()
    
    # Split input into a list where each list entry is a single line from the 
    # input text file. Each list entry of a single line to be split to a 
    # secondary list of characters contained within that line in the input text
    
    geoList1 = inputContent.split("\n")
    
    geoList2 = []
    
    for i in geoList1:
        geoList2.append(list(i))
        
    # geoList2 to be considered an array of coordinates. Entries in geoList2 
    # constitute the vertical axis (y), entries within each sub-slist constitute
    # the horizontal axis (x). The start position will be y = 0, x = 0.
    x = 0
    y = 0
    
    # Set the maximum bounds for both the x and y axis. 
    # Although the geological pattern repeats an unknown number of the times to 
    # the right of the start position, it repeats in the SAME pattern. 
    # The max bound will be used to enable us to loop back to the horizontal 
    # start position of the pattern.
    # The max x axis bound will be the length of the list held in the first 
    # position of the geoList2 list.
    # The maximum bound of the y axis will be used to identify when the bottom
    # of the slope is reached. This will be the lenght of geoList2
    # As we're moving through indexes in a list, subtract 1 from the lengths
    # as indexes begin at 0
    maxX = len(geoList2[0]) - 1
    maxY = len(geoList2) - 1
    
    # Initialise count of trees hit to 0
    trees = 0
    
    # Iterate through geoList2 until the number of steps taken down the slope
    # equals the value for maxY
    while y < maxY:
        
        # If moving x exceeds the max bound for x, loop back to the beginning
        # Subtract 1 to account for 0 indexing in lists
        if x + moveX > maxX:
            x = ((x + moveX) - maxX) - 1
        # Move x by the passed in value if it does not exceed the max value 
        # for x    
        else: 
            x = x + moveX
        
        # Move y by the value passed in    
        y += moveY
        
        # Check character at the coordinates given by x and y
        if geoList2[y][x] == "#":
            # Increment count of trees hit if character is #
            trees += 1
            
        # If character is not #, do nothing and continue loop
        
    return trees
            
            
    
print(tobogganTrajectory(1, 2))