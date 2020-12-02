# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 18:54:45 2020

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
    # The first position in the list will be the character positions to check 
    #(NOT zero indexed), the second position will be the character to check for
    # and the third position will be the password to check.
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
        
        # Set the positions to define which characters of the password to check,
        # removing the hyphen between the two numbers. Split string to list with
        # two positions based on the hyphen
        charPositions = j[0].split("-")
        
        # Convert both check positions to ints. Subtract 1 from each as
        # passwords are not zero indexed
        charPos1 = int(charPositions[0]) - 1
        charPos2 = int(charPositions[1]) - 1
        
        # Initialise the number of matched characters found to 0
        charMatch = 0        
        
        # Check if the character in the first check position of the password 
        # matches the check character
        if password[charPos1] == checkChar:
            
            # Increment number of matched characters found
            charMatch += 1
        
        # Check if the character in the second check position of the password 
        # matches the check character
        if password[charPos2] == checkChar:
            
            # Increment number of matched characters found
            charMatch += 1
          
        # Check if only one of the check positions contained the check character    
        if charMatch == 1:
            
            # Increment number of valid passwords found
            validPass += 1
            
    # Return the number of valid passwords found        
    return validPass

print(passPhil())