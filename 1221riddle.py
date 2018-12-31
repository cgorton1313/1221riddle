print("Starting...")
stringToProcess = "1"
print(stringToProcess)
newString = ""

def countEqualChars(subArray):
  foundSimilar = False;
  count = 1
  number = subArray[0]

  while (not foundSimilar):
    if (len(subArray) > count):
      if (subArray[count] == number):
        count += 1
      else:
        foundSimilar = True
    else:
      foundSimilar = True
  
  return {'number':number, 'count':count}

for i in range(0,12):
  theArray = list(stringToProcess)
  while (len(theArray) != 0):
    thisCount = countEqualChars(theArray)
    newString += str(thisCount["count"]) + str(thisCount["number"])
    theArray = theArray[thisCount["count"]:]
  stringToProcess = newString;
  print(stringToProcess)
  newString = ""

print("Done!")