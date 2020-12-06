# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 13:39:07 2020

@author: David Stanley
"""
import math

def binaryBoarding():  
    
    # Read input text file and store contents
    inputText = open("input.txt", "r")
    inputContent = inputText.read()
    
    # Close opened file
    inputText.close()
    
    # Split input text to a list of seat positions
    seatPositions = inputContent.split("\n")
    
    # Create list to store calculated seat IDs
    seatIDList = []
    
    # Iterate over seat positions
    for seat in seatPositions:
        # Set maximum and minimum rows/columns
        maxRow = 127
        minRow = 0
        maxColumn = 7
        minColumn = 0
        
        # Separate row and column identifiers from seat position string
        rowString = seat[:7]
        columnString = seat[-3:]
        
        # Iterate over characters in row identifier
        for r in rowString:
            # Check if character is F
            if r == "F":
                # Keep only the first/lower half of the possible row range
                maxRow = math.floor((minRow + maxRow) / 2)
            # Check if character is B
            elif r == "B":
                # Keep the second/higher half of the possible row range
                minRow = math.ceil((minRow + maxRow) / 2)
        
        # Iterate over characters in column identifier
        for c in columnString:
            # Check if character is L
            if c == "L":
                # Keep the left/lower half ov the possible column range
                maxColumn = math.floor((minColumn + maxColumn) / 2)
            # Check if character is R
            elif c == "R":
                # Keep the right/upper half of the possible column range
                minColumn = math.ceil((minColumn + maxColumn) / 2)
        
        # Max and max values for row and column should now be the same.
        # Set row and column to be the min for each
        row = minRow
        column = minColumn
        
        # Calculate seat id - multiply the row by 8 then add the column
        seatID = (row * 8) + column
        
        # Store the seat ID in the seat ID list
        seatIDList.append(seatID)
        
    # Return the highest value stored in the seat ID list
    return max(seatIDList)
        

print(binaryBoarding())