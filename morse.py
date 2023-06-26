import ctypes

# cpplibrary = ctypes.CDLL("/home/marinos/Desktop/morseCoder/cppMorse.so")

def findTransmissionRate(pos, bit, morseString):
    size = 0
    for index, value in enumerate(morseString[pos:], pos):
        if value == bit:
            size += 1
        else:
            break
    return size, index


bitsMorseString = "1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011"
bitsMorseString = bitsMorseString.strip('0')  # remove possible zeroes from the begin and end of the string
decodedString = ""

transmissionRate = 1   # the 'default' and correct transmission rate of the bitMorseCode
sizeOfMorseBit, indexOfNextBit = findTransmissionRate(bitsMorseString.find('1'), '1', bitsMorseString)

if sizeOfMorseBit == 2:
    transmissionRate = 2

elif sizeOfMorseBit>2: # if the size of the 1's bits is bigger than 2, I don't if it has transmission rate or not e.g. if there are 3 1's at he beggining, is it dot'.' with tranmissionRate==3, or is it dash "-" which has 3 1's for decoding?
    # call the function to check the logic of the transmission rate
    tempHelp = 0
    sizeOfMorseBit2, indexOfNextBit2 = findTransmissionRate(indexOfNextBit, '0', bitsMorseString)
    while sizeOfMorseBit == sizeOfMorseBit2:
        toggle = bool(tempHelp % 2)
        bit = '0' if toggle else '1'
        sizeOfMorseBit2, indexOfNextBit2 = findTransmissionRate(indexOfNextBit2, bit, bitsMorseString)
        tempHelp += 1
    rate = sizeOfMorseBit / 3
    if sizeOfMorseBit2 / rate == 1.0 or sizeOfMorseBit2 / rate == 7.0:
        transmissionRate = int(rate)

print("The transmissionRate of this string is: ", transmissionRate)

# create the correct morseBits after the transmissionRate
zerosSubstring = transmissionRate * "0"
onesSubstring = transmissionRate * "1"
subString = ""
for i in range (0, len(bitsMorseString), transmissionRate):
    subString = bitsMorseString[i:i+transmissionRate]  #from the current position of the index, until (:) the size of the transmissionRate ==> create a substring to check the bits
    if subString == onesSubstring:
        decodedString += "1"
    
    elif subString == zerosSubstring:
        decodedString += "0"
#########################################################################################
# Until here I find the proper bits representation of a coded morse code

morseString = ""
dashMorse = "111"
dotMorse = "1"
pauseBetweenWords = "0000000"
pauseBetweenChars = "000"
pauseBetweenSymbols = "0"
i=0

while i < len(decodedString):
    # check for ones
    if dashMorse == decodedString[i:i+3]:
        morseString += "-"
        i += 3
        continue
    elif dotMorse == decodedString[i]:
        morseString += "."
        i += 1
        continue

    # check for zeroes
    if pauseBetweenWords == decodedString[i:i+7]:
        morseString += "   "
        i += 7
    elif pauseBetweenChars == decodedString[i:i+3]:
        morseString += " "
        i += 3
    elif pauseBetweenSymbols == decodedString[i]:
        i += 1
#########################################################################################
# Until here I find the proper form of Morse code with dots and dashes. morseString contains the form with dots '.' and dashed '-'

print(morseString)
# from here I pass the variable to the c++ function and it will print the human string

















#deprecated
# i = 0
# while i < (len(decodedString)-1): 
#         if i == len(decodedString):
#             if decodedString[i] == "1":
#                 morseString += "."
#             else:
#                 break

#         if decodedString[i] == "1":
#             if decodedString[i+1] == "1":
#                 if decodedString[i+2] == "1":
#                     morseString += "-"
#                     i += 3
            
#             elif decodedString[i+1] == "0": # after one '1', we found a '0' which means it is a dot '.'
#                 morseString += "."
#                 i += 2

#         else:
#             if decodedString[i-1] == "0" and decodedString[i+1] == "0":
#                 morseString += " "
#                 i += 2
            
#             elif decodedString[i-1] == "1" and decodedString[i+1] == "1":
#                 i += 1
            
#             elif decodedString[i-1] == "1" and decodedString[i+1] == "0":
#                 if decodedString[i+2] == "0" and decodedString[i+3] == "0":
#                     i += 7
#                     morseString += "   " 
#                 elif decodedString[i+2] == "0":
#                     i += 3
#                     morseString += " "
# print("The morse code from the previous bit-encoded representation is: ", morseString, '\n')
