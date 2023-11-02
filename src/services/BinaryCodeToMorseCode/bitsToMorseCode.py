# Bits to morse python file
from src.services.BinaryCodeToMorseCode import convertBinaryToMorseSymbols


def findNumberOfBitsPerGroup(pos, bit, morseString):
    size = 0
    for index, value in enumerate(morseString[pos:], pos):
        if value == bit:
            size += 1
        else:
            break
    return size, index


def findTransmissionRate(stringOfBits):
    stringOfBits = stringOfBits.strip('0')  # remove possible zeroes from the beginning and end of the string
    transmissionRate = 1  # the 'default' and correct transmission rate of the stringOfBits variable is: 1

    sizeOfMorseBit, indexOfNextBit = findNumberOfBitsPerGroup(stringOfBits.find('1'), '1', stringOfBits)
    if sizeOfMorseBit == 2:
        transmissionRate = 2

    elif sizeOfMorseBit >= 3:  # if the size of the 1's bits is bigger than 2, I don't know if it has transmission rate or not e.g. if there are 3 1's at he beginning, is it dot'.' with transmissionRate==3, or is it dash "-" which has 3 1's for decoding?
        toggle = False
        sizeOfMorseBit2, indexOfNextBit2 = findNumberOfBitsPerGroup(indexOfNextBit, '0', stringOfBits)

        while sizeOfMorseBit == sizeOfMorseBit2:
            bit = '0' if toggle else '1'
            sizeOfMorseBit2, indexOfNextBit2 = findNumberOfBitsPerGroup(indexOfNextBit2, bit, stringOfBits)
            toggle = not toggle

        if sizeOfMorseBit2 == 0:
            transmissionRate = sizeOfMorseBit

        elif sizeOfMorseBit > sizeOfMorseBit2:
            transmissionRate = sizeOfMorseBit2

        elif sizeOfMorseBit < sizeOfMorseBit2:
            transmissionRate = sizeOfMorseBit

    return transmissionRate


def createBinaryMorseStringWithoutRate(stringOfBits, transmissionRate):  # create the correct morseBits after the transmissionRate
    binaryStringWithoutTransmissionRate = ""
    zerosSubstring = transmissionRate * "0"
    onesSubstring = transmissionRate * "1"
    subString = ""
    for i in range(0, len(stringOfBits), transmissionRate):
        subString = stringOfBits[i:i + transmissionRate]  # from the current position of the index, until (:) the size of the transmissionRate ==> create a substring to check the bits
        if subString == onesSubstring:
            binaryStringWithoutTransmissionRate += "1"

        elif subString == zerosSubstring:
            binaryStringWithoutTransmissionRate += "0"

    return binaryStringWithoutTransmissionRate


def convertBitsToDotsDashes(stringOfBits):
    transmissionRate = findTransmissionRate(stringOfBits)
    print("The transmissionRate of this string is: ", transmissionRate)

    # Find the proper bits representation of a coded morse code, without transmission rate
    decodedString = createBinaryMorseStringWithoutRate(stringOfBits, transmissionRate)
    print("The proper bits representation is {0}\n".format(decodedString))

    morseCodeString = convertBinaryToMorseSymbols.createProperMorseCodeString(decodedString)
    
    return morseCodeString
   