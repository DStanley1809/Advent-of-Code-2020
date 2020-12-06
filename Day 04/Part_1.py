# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 19:08:52 2020

@author: David Stanley
"""

    

class passport(object):
    
    def __init__(self, byr, cid, ecl, eyr, hcl, hgt, iyr, pid):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid
    
    # When called, return the value held for each property
    def getByr(self):
        return self.byr
        
    def getIyr(self):
        return self.iyr
        
    def getEyr(self):
        return self.eyr
        
    def getHgt(self):
        return self.hgt
        
    def getHcl(self):
        return self.hcl
        
    def getEcl(self):
        return self.ecl
        
    def getPid(self):
        return self.pid
        
    def getCid(self):
        return self.cid
    
    # CID property is optional. Passport must hold valid value for all remaining
    # properties. Check that all other properties are not None.    
    def isValid(self):
        return self.getByr() is not None and self.getIyr() is not None and\
            self.getEyr() is not None and self.getHgt() is not None and\
                self.getHcl() is not None and self.getEcl() is not None and\
                    self.getPid() is not None


def passportProcessing():
    
    # Read input text file and store contents
    inputText = open("input.txt", "r")
    inputContent = inputText.read()
    
    # Close opened file
    inputText.close()
    
    # Split input file into list of passports
    passportList = inputContent.split("\n\n")
    
    # Create new list to store passport information after further splitting
    passportList2 = []
    
    # Iterate over entries in passportList, replace any new line characters
    # with spaces then split the string on spaces. Append each split list to 
    # passportList2
    for i in passportList: 
        passportList2.append((i.replace("\n", " ").split(" ")))
        
    # Iterate over passportList2, sort and store information held in each 
    # passport alphabetically
    passportCounter = 0
    for j in passportList2:
        passportList2[passportCounter] = sorted(j)
        passportCounter += 1
        
    # Create a list to store created passport objects
    passportObjectList = []
    
    # Iterate over passportList2
    for k in passportList2:
        # Initialise each data type to None
        byr = None
        cid = None
        ecl = None
        eyr = None
        hcl = None
        hgt = None
        iyr = None
        pid = None
        
        # Iterate over entry in the sublist k
        for l in k:
            # Check first three characters of each entry and assign the data
            # to the matching variable
            if l[:3] == "byr":
                byr = l[4:]
                
            elif l[:3] == "cid":
                cid = l[4:]
                
            elif l[:3] == "ecl":
                ecl = l[4:]
            
            elif l[:3] == "eyr":
                eyr = l[4:]
            
            elif l[:3] == "hcl":
                hcl = l[4:]
            
            elif l[:3] == "hgt":
                hgt = l[4:]
            
            elif l[:3] == "iyr":
                iyr = l[4:]
            
            elif l[:3] == "pid":
                pid = l[4:]
                
        # Create a passport object, passing in the values currently held
        # for each data type
        passportObj = passport(byr, cid, ecl, eyr, hcl, hgt, iyr, pid)
        
        # Append created passport object to list of passport objects
        passportObjectList.append(passportObj)
            
    # Create variable to count number of valid passports found, initialised to
    # 0
    validPassports = 0
    
    # Iterate over all passport objects
    for passports in passportObjectList:
        # If passport is valid
        if passports.isValid():
            validPassports += 1
    
    # Return the number of valid passports found
    return validPassports
                
print(passportProcessing())









            
        
        
        
    
    
    