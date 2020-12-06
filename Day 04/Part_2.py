# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 19:08:52 2020

@author: David Stanley
"""

import string
    

class passport(object):
    
    # Initialise object using values passed in when called
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
    
    # Check validity of each property
    # Birth year valid if value between 1920 and 2002. Invalid if None or
    # outside of range
    def isByrValid(self):
        if self.getByr() == None:
            return False
        else:
            birthYear = int(self.getByr())
            return birthYear >= 1920 and birthYear <= 2002
        
    # Issue year valid if value between 2010 and 2020. Invalid if None or
    # outside of range
    def isIyrValid(self):
        if self.getIyr() == None:
            return False        
        else:
            issueYear = int(self.getIyr())
            return issueYear>= 2010 and issueYear <= 2020
    
    # Expiry year valid if between 2020 and 2030. Invalid if None or outside
    # range
    def isEyrValid(self):
        if self.getEyr() == None:
            return False
        else:
            expirationYear = int(self.getEyr())
            return expirationYear >= 2020 and expirationYear <= 2030
    
    # If height in cm, valid if between 150 and 193.
    # If height in inches, valid if between 59 and 76.
    # Invalid if outside of ranges or None
    def isHgtValid(self):
        if self.getHgt() == None:
            return False
        else:
            if self.getHgt()[-2:] == "cm" and len(self.getHgt()[:-2]) == 3:
                height = int(self.getHgt()[:3])
                return height >= 150 and height <= 193
            elif self.getHgt()[-2:] == "in" and len(self.getHgt()[:-2]) == 2:
                height = int(self.getHgt()[:2])
                return height >= 59 and height <= 76
     
    # Hair colour valid if begins with "#" and has exactly 6 alphanumeric
    # digits following. Invalid if None or doesn't comply with requirements
    def isHclValid(self):
        if self.getHcl() == None:
            return False
        if len(self.getHcl()) != 7:
            return False
        else:
            validChars = string.ascii_lowercase + string.digits
            if self.getHcl()[:1] == "#":
                hairColourCode = self.getHcl()[1:]
                
                validCharCount = 0
                for c in hairColourCode:
                    if c in validChars:
                        validCharCount += 1
                
                return validCharCount == 6
    
    # Eye colour valid if colours code in list of permitted hair colour codes.
    # Invalid if None or not in permitted list
    def isEclValid(self):
        if self.getEcl() == None:
             return False
         
        else:
            validEyeColours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            return self.getEcl() in validEyeColours
    
    # Passport ID valid if comprised of exactly 9 numeric digits. Invalid if 
    # not 9 numeric digits or None.
    def isPidValid(self):
        if self.getPid() == None:
            return False
        if len(self.getPid()) != 9:
            return False
        else:
            validNumbers = string.digits
            validNumbersCount = 0
            for n in self.getPid():
                if n in validNumbers:
                    validNumbersCount += 1
            
            return validNumbersCount == 9
            
        
                
    
    # CID property is optional. Passport must hold valid values for all remaining
    # properties. Call validity checker for each property. If a property is
    # valid, increment valid property counter. Passport is valid if it has
    # 7 valid properties
    def isPassportValid(self):
        validPropertyCount = 0
        
        if self.isByrValid() == True:
            validPropertyCount += 1
        
        if self.isIyrValid() == True:
            validPropertyCount += 1
        
        if self.isEyrValid() == True:
            validPropertyCount += 1
        
        if self.isHgtValid() == True:
            validPropertyCount += 1
        
        if self.isHclValid() == True:
            validPropertyCount += 1
        
        if self.isEclValid() == True:
            validPropertyCount += 1
        
        if self.isPidValid() == True:
            validPropertyCount += 1
            
        return validPropertyCount == 7
        


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
        if passports.isPassportValid():
            validPassports += 1
    
    # Return the number of valid passports found
    return validPassports
                
print(passportProcessing())









            
        
        
        
    
    
    