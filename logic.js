console.log("Starting...");
var stringToProcess = "1";
console.log(stringToProcess);
var newString = "";

for (var i = 0; i < 20; i++) {
    var theArray = stringToProcess.split('');
    while (theArray.length != 0) {
        var thisCount = countEqualChars(theArray);
        newString += thisCount.count.toString() + thisCount.number;
        theArray.splice(0, thisCount.count);
    }
    stringToProcess = newString;
    console.log(stringToProcess);
    newString = "";
}

function countEqualChars(subArray) {
    var foundSimilar = false;
    var count = 1;
    var number = subArray[0];
    while (!foundSimilar) {
        if (subArray[count] == number) {
            count++;
        } else {
            foundSimilar = true;
        }
    }
    return {number: number, count: count};
}