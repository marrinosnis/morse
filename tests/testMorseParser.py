from src.BinaryCodeToMorseCode import bitsToMorseCode, convertBinaryToMorseSymbols
from tests import morseModule

with open('../src/binaryMorseCode.txt', 'r') as binaryCodeTr:
    binaryMorseCodeWithTransmission = [line.strip() for line in binaryCodeTr]

with open('dataToBeTested/binaryCodeNoTransmission.txt', 'r') as binaryCodeNoTr:
    binaryMorseCodeWithoutTransmission = [line.strip() for line in binaryCodeNoTr]

with open('dataToBeTested/morseCode.txt', 'r') as morseCode:
    finalMorseCode = [line.strip() for line in morseCode]


morseCodeData = {
    'firstText':  [5, "1110001010101000100000001110111010111000101011100010100011101011101000111010111000000011101010100010111010001110111011100010111011100011101000000010101110100011101110111000111010101110000000101110111011100010101110001110111000101110111010001010100000001110111011100010101011100010001011101000000011100010101010001000000010111010100010111000111011101010001110101110111000000011101010001110111011100011101110100010111010111010111", "- .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-", "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG."],
    'secondText': [2, "10101010001000111010111011100000001011101110111000101011100011101010001", ".... . -.--   .--- ..- -.. .", "HEY JUDE"],
    'thirdText':  [6, "10101010001000111010111011100000001011101110111000101011100011101010001", ".... . -.--   .--- ..- -.. .", "HEY JUDE"],
    'forthText':  [1, "1110001010101000100000001110111010111000101011100010100011101011101000111010111000000011101010100010111010001110111011100010111011100011101000000010101110100011101110111000111010101110000000101110111011100010101110001110111000101110111010001010100000001110111011100010101011100010001011101000000011100010101010001000000010111010100010111000111011101010001110101110111000000011101010001110111011100011101110100010111010111010111", "- .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-", "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG."],
    'fifthText':  [1, "1011101010001000101110001011101000111010000000111011100011101110111000101110100010101000100010101110111010111000111010111010001110111011100011101010001", ".-.. . .- .-. -.   -- --- .-. ... . ..--.- -.-. --- -.. .", "LEARN MORSE_CODE"]

}
# TODO1 PERFORM A REFACTOR TO THE WAY OF TESTING
# TODO2 ADD FAILED SCENARIOS


def testFindTransmissionRate():
    assert bitsToMorseCode.findTransmissionRate(binaryMorseCodeWithTransmission[0]) == morseCodeData['firstText'][0]
    assert bitsToMorseCode.findTransmissionRate(binaryMorseCodeWithTransmission[1]) == morseCodeData['secondText'][0]
    assert bitsToMorseCode.findTransmissionRate(binaryMorseCodeWithTransmission[2]) == morseCodeData['thirdText'][0]
    assert bitsToMorseCode.findTransmissionRate(binaryMorseCodeWithTransmission[3]) == morseCodeData['forthText'][0]
    assert bitsToMorseCode.findTransmissionRate(binaryMorseCodeWithTransmission[4]) == morseCodeData['fifthText'][0]


def testBinaryNoTransmissionRate():
    assert bitsToMorseCode.createBinaryMorseStringWithoutRate(binaryMorseCodeWithTransmission[0], 5) == morseCodeData['firstText'][1]
    assert bitsToMorseCode.createBinaryMorseStringWithoutRate(binaryMorseCodeWithTransmission[1], 2) == morseCodeData['secondText'][1]
    assert bitsToMorseCode.createBinaryMorseStringWithoutRate(binaryMorseCodeWithTransmission[2], 6) == morseCodeData['thirdText'][1]
    assert bitsToMorseCode.createBinaryMorseStringWithoutRate(binaryMorseCodeWithTransmission[3], 1) == morseCodeData['forthText'][1]
    assert bitsToMorseCode.createBinaryMorseStringWithoutRate(binaryMorseCodeWithTransmission[4], 1) == morseCodeData['fifthText'][1]


def testCreateProperMorseCodeString():
    assert convertBinaryToMorseSymbols.createProperMorseCodeString(binaryMorseCodeWithoutTransmission[0]) == morseCodeData['firstText'][2]
    assert convertBinaryToMorseSymbols.createProperMorseCodeString(binaryMorseCodeWithoutTransmission[1]) == morseCodeData['secondText'][2]
    assert convertBinaryToMorseSymbols.createProperMorseCodeString(binaryMorseCodeWithoutTransmission[2]) == morseCodeData['thirdText'][2]
    assert convertBinaryToMorseSymbols.createProperMorseCodeString(binaryMorseCodeWithoutTransmission[3]) == morseCodeData['forthText'][2]
    assert convertBinaryToMorseSymbols.createProperMorseCodeString(binaryMorseCodeWithoutTransmission[4]) == morseCodeData['fifthText'][2]


def testMorseResults():
    mr = morseModule.DecodeMorseCode()
    assert mr.decodeMorse(finalMorseCode[0]) == morseCodeData['firstText'][3]
    assert mr.decodeMorse(finalMorseCode[1]) == morseCodeData['secondText'][3]
    assert mr.decodeMorse(finalMorseCode[2]) == morseCodeData['thirdText'][3]
    assert mr.decodeMorse(finalMorseCode[3]) == morseCodeData['forthText'][3]
    assert mr.decodeMorse(finalMorseCode[4]) == morseCodeData['fifthText'][3]


