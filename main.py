import os
import random

absDirPath = "C:\\Users\\yorishori\\Documents\\My Documents\\Projects\\Writting\\Literary\\Phrase\\"
staticName = "Phrase"

def generateRandoms(length: int, numberSet:list = list()) -> list:
    internalSet = numberSet.copy()
    
    while len(internalSet) < length + 2:
        rndNum = random.randint(16, 17+(length * 2))
        if rndNum not in internalSet:
            internalSet.append(rndNum)

    return internalSet



filesInPath = os.listdir(absDirPath)

# Rename all files to temporary names
rndNumbersList = generateRandoms(len(filesInPath))
for i in range(len(filesInPath)):
    # Get filename and path
    fileName = filesInPath[i]
    filePath = absDirPath+fileName
    # Check that it's a file
    if os.path.isfile(filePath):
        # Get extension, if any
        try:
            fileExtension = fileName[fileName.rindex('.'):]
        except ValueError:
            fileExtension = ""
        # Rename file
        os.rename((filePath),(absDirPath+fileName+".temp"))
    

filesInPath = os.listdir(absDirPath)

# Give the new names
rndNumbersList = generateRandoms(len(filesInPath))
for i in range(len(filesInPath)):
    # Get filename and path
    fileName = filesInPath[i]
    filePath = absDirPath+fileName
    # Check that it's a file
    if os.path.isfile(filePath):
        # Get extension, if any
        try:
            fileExtension = fileName[fileName.rindex('.'):]
        except ValueError:
            fileExtension = ""
        # Rename file to definitive name
        hexNum = str(hex(rndNumbersList[i])).upper().replace('0X','_')
        os.rename((filePath),(absDirPath+staticName+hexNum+fileExtension))
