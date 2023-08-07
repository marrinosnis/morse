# Bits to morse python file
from BinaryCodeToMorseCode import convertBinaryToMorseSymbols


def find_transmission_rate(pos, bit, morseString):
    size = 0
    for index, value in enumerate(morseString[pos:], pos):
        if value == bit:
            size += 1
        else:
            break
    return size, index


def convertBitsToDotsDashes(stringOfBits):  # this is wrong. Here I find the correct representation of the zeroes and ones
    stringOfBits = stringOfBits.strip('0')  # remove possible zeroes from the beginning and end of the string
    decodedString = ""
    transmissionRate = 1   # the 'default' and correct transmission rate of the stringOfBits variable is: 1

    sizeOfMorseBit, indexOfNextBit = find_transmission_rate(stringOfBits.find('1'), '1', stringOfBits)
    if sizeOfMorseBit == 2:
        transmissionRate = 2

    elif sizeOfMorseBit >= 3:  # if the size of the 1's bits is bigger than 2, I don't know if it has transmission rate or not e.g. if there are 3 1's at he beginning, is it dot'.' with transmissionRate==3, or is it dash "-" which has 3 1's for decoding?
        toggle = False
        sizeOfMorseBit2, indexOfNextBit2 = find_transmission_rate(indexOfNextBit, '0', stringOfBits)
        
        while sizeOfMorseBit == sizeOfMorseBit2:
            bit = '0' if toggle else '1'
            sizeOfMorseBit2, indexOfNextBit2 = find_transmission_rate(indexOfNextBit2, bit, stringOfBits)
            toggle = not toggle
        
        if sizeOfMorseBit2 == 0:
            transmissionRate = sizeOfMorseBit
        
        elif sizeOfMorseBit > sizeOfMorseBit2:
            transmissionRate = sizeOfMorseBit2
        
        elif sizeOfMorseBit < sizeOfMorseBit2:
            transmissionRate = sizeOfMorseBit

    print("The transmissionRate of this string is: ", transmissionRate)

    # create the correct morseBits after the transmissionRate
    zerosSubstring = transmissionRate * "0"
    onesSubstring = transmissionRate * "1"
    subString = ""
    for i in range(0, len(stringOfBits), transmissionRate):
        subString = stringOfBits[i:i+transmissionRate]  # from the current position of the index, until (:) the size of the transmissionRate ==> create a substring to check the bits
        if subString == onesSubstring:
            decodedString += "1"
        
        elif subString == zerosSubstring:
            decodedString += "0"
    # Until here I find the proper bits representation of a coded morse code

    print("The proper bits representation is {0}\n".format(decodedString))
    morseCodeString = convertBinaryToMorseSymbols.createProperMorseCodeString(decodedString)
    
    return morseCodeString
   