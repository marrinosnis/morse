from BinaryCodeToMorseCode import bitsToMorseCode, convertBinaryToMorseSymbols
import morseModule

with open('../binaryMorseCode.txt', 'r') as binaryCode:
    transmissionRate = [line.strip() for line in binaryCode]

# with open('../morseCodeSymbols.txt', 'r') as morseSymbols:
#     morseCode = [line.strip() for line in morseSymbols]

with open('expectedText.txt', 'r') as text:
    humanString = [line.strip() for line in text]


def testFindTransmissionRate():
    assert bitsToMorseCode.findTransmissionRate(transmissionRate[0]) == 5
    assert bitsToMorseCode.findTransmissionRate(transmissionRate[1]) == 2


def testCreateProperMorseCodeString():
    assert convertBinaryToMorseSymbols.createProperMorseCodeString("10101010001000111010111011100000001011101110111000101011100011101010001") == ".... . -.--   .--- ..- -.. ."


def testMorseResults():
    mr = morseModule.DecodeMorseCode()
    print('\n', humanString[0])
    assert mr.decodeMorse("- .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-") == humanString[0]
