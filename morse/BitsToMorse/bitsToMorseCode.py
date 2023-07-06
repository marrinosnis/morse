# Bits to morse python file

def findTransmissionRate(pos, bit, morseString):
    size = 0
    for index, value in enumerate(morseString[pos:], pos):
        if value == bit:
            size += 1
        else:
            break
    return size, index

def convertBinaryToMorseCode(binaryString):
    morseString = ""
    dashMorse = "111"
    dotMorse = "1"
    pauseBetweenWords = "0000000"
    pauseBetweenChars = "000"
    pauseBetweenSymbols = "0"
    i=0

    while i < len(binaryString):
        # check for ones
        if dashMorse == binaryString[i:i+3]:
            morseString += "-"
            i += 3
            continue
        elif dotMorse == binaryString[i]:
            morseString += "."
            i += 1
            continue

        # check for zeroes
        if pauseBetweenWords == binaryString[i:i+7]:
            morseString += "   "
            i += 7
        elif pauseBetweenChars == binaryString[i:i+3]:
            morseString += " "
            i += 3
        elif pauseBetweenSymbols == binaryString[i]:
            i += 1
    
    return morseString
    # Find the proper form of Morse code with dots and dashes. morseString contains the form with dots '.' and dashed '-'



def convertBitsToDotsDashes(stringOfBits):
    stringOfBits = stringOfBits.strip('0')  # remove possible zeroes from the begin and end of the string
    decodedString = ""

    transmissionRate = 1   # the 'default' and correct transmission rate of the stringOfBits is: 1
    sizeOfMorseBit, indexOfNextBit = findTransmissionRate(stringOfBits.find('1'), '1', stringOfBits)

    if sizeOfMorseBit == 2:
        transmissionRate = 2

    elif sizeOfMorseBit>2: # if the size of the 1's bits is bigger than 2, I don't know if it has transmission rate or not e.g. if there are 3 1's at he beggining, is it dot'.' with tranmissionRate==3, or is it dash "-" which has 3 1's for decoding?
        tempHelp = 0
        sizeOfMorseBit2, indexOfNextBit2 = findTransmissionRate(indexOfNextBit, '0', stringOfBits)
        while sizeOfMorseBit == sizeOfMorseBit2:
            toggle = bool(tempHelp % 2)
            bit = '0' if toggle else '1'
            sizeOfMorseBit2, indexOfNextBit2 = findTransmissionRate(indexOfNextBit2, bit, stringOfBits)
            tempHelp += 1
        rate = sizeOfMorseBit / 3
        if sizeOfMorseBit2 / rate == 1.0 or sizeOfMorseBit2 / rate == 7.0:
            transmissionRate = int(rate)

    print("The transmissionRate of this string is: ", transmissionRate)

    # create the correct morseBits after the transmissionRate
    zerosSubstring = transmissionRate * "0"
    onesSubstring = transmissionRate * "1"
    subString = ""
    for i in range (0, len(stringOfBits), transmissionRate):
        subString = stringOfBits[i:i+transmissionRate]  #from the current position of the index, until (:) the size of the transmissionRate ==> create a substring to check the bits
        if subString == onesSubstring:
            decodedString += "1"
        
        elif subString == zerosSubstring:
            decodedString += "0"
     # Until here I find the proper bits representation of a coded morse code


    morseCodeString = convertBinaryToMorseCode(decodedString)
    
    return morseCodeString
   