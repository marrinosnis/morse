from BinaryCodeToMorseCode import bitsToMorseCode
import morseModule  # this is from the .cpp file that is created as a python module. The morse is the morse.so

with open('binaryMorseCode.txt', 'r') as binaryCode:
    binaryMorseCode = [line for line in binaryCode]

morseString = bitsToMorseCode.convertBitsToDotsDashes(binaryMorseCode[1])
print("The final morse code form is: {0}\n".format(morseString))

# from here I pass the variable to the c++ function, and it will print the human string
mr = morseModule.DecodeMorseCode()
humanString = mr.decodeMorse(morseString)

with open('tests/expectedText.txt', 'r') as file:
    text = file.readline()
    text = text.strip()  # remove any possible newline characters '\n' from the tail of the string, in order to do a correct assertion

print("The respective human string is: {0}".format(humanString))
print("The original text is          : {0}".format(text))

if humanString == text:
    print("The decoder works fine")
else:
    print("shit SHIT shit")

