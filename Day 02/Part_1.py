# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 13:45:39 2020

@author: David Stanley
"""

def passPhil():
    
    # Read input text file and store contents
    inputText = open("input.txt", "r")
    inputContent= inputText.read()
    
    # Close opened file
    inputText.close()
    
    # Split input text in to a list based on line breaks. Each line/list entry
    # represents one user's password and the policy against which to check it
    inputList = inputContent.split("\n")
    
    # Split each user string in to an individual list based on space characters.
    # The first position in the list will be the minimum and maximum allowable 
    # instances of the check character the second position will be the 
    # character to check for and the third position will be the password to check.
    userList = []
    
    for i in inputList:
        userList.append(i.split(" "))
        
    # Create variable to count number of valid passwords found
    validPass = 0
        
    # Iterate over each user/password
    for j in userList:
        # Set the password to be the third position in the list
        password = j[2]
        
        # Set the character to be checked for. Remove the colon at the end of 
        # the string
        checkChar = j[1][:-1]
        
        # Set the minimum and maximum allowable counts of the check character. 
        # Split the min/max string based on the hyphen 
        charMinMax = j[0].split("-")
        
        # Convert the minimum and maximum values to ints and store ints as 
        # new min/max variables
        charMinCount = int(charMinMax[0])
        charMaxCount = int(charMinMax[1])
        
        # Count the number of times the check character appears in the password
        checkCharCount = password.count(checkChar)
        
        # Check if the check character count is within the minimum and maximum 
        # bounds
        if checkCharCount >= charMinCount and checkCharCount <= charMaxCount:
            
            # Increment the number of valid passwords found
            validPass += 1
    
    # Return the number of valid passwords found
    return validPass

print(passPhil())