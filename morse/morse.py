from BitsToMorse import bitsToMorseCode
import morse

temp = "1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011"

morseString = bitsToMorseCode.convertBitsToDotsDashes(temp)

print(morseString)
# from here I pass the variable to the c++ function and it will print the human string

mr = morse.MorseDecoderString()
humanString = mr.decodeMorse(morseString)

print("The respective human string is:\n", humanString)

    