from src.services.BinaryCodeToMorseCode import bitsToMorseCode
import os
import morseModule  # this is from the .cpp file that is created as a python module. The morseModule is the morseModule.so

dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir_path, '../binaryMorseCode.txt')

with open(file_path, 'r') as binaryCode:
    binaryMorseCode = [line for line in binaryCode]

morseString = bitsToMorseCode.convertBitsToDotsDashes(binaryMorseCode[4])
print("The final morse code form is: {0}\n".format(morseString))

# from here I pass the variable to the c++ function, and it will print the human string
mr = morseModule.DecodeMorseCode()
humanString = mr.decodeMorse(morseString)

print("The respective human readable string is: {0}".format(humanString))
