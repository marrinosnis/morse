MORSE_CODE = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    ".-.-.-": ".",
    "--..--": ",",
    "..--..": "?",
    ".----.": ",",
    "-.-.--": "!",
    "-..-.": "/",
    "-.--.": "(",
    "-.--.-": ")",
    ".-...": "",
    "---...": ":",
    "-.-.-.": ";",
    "-...-": "=",
    ".-.-.": "",
    "-....-": "-",
    "..--.-": "_",
    ".-..-.": "\"",
    "...-..-": "",  # //wait (??? ti einai auto? )
    ".--.-.": "@",
    "...---...": "SOS"
}


def find_transmission_rate(pos, bit, morseString):
    size = 0
    for index, value in enumerate(morseString[pos:], pos):
        if value == bit:
            size += 1
        else:
            break
    return size, index


def decode_bits(bits):
    bits = bits.strip('0')  # remove possible zeroes from the beginning and end of the string
    decodedString = ""

    print(bits)
    transmissionRate = 1  # the 'default' and correct transmission rate of the bitMorseCode
    sizeOfMorseBit, indexOfNextBit = find_transmission_rate(bits.find('1'), '1', bits)

    if sizeOfMorseBit == 2:
        transmissionRate = 2

    elif sizeOfMorseBit >= 3:
        tempHelp = 0
        sizeOfMorseBit2, indexOfNextBit2 = find_transmission_rate(indexOfNextBit, '0', bits)

        while sizeOfMorseBit == sizeOfMorseBit2:
            toggle = bool(tempHelp % 2)
            bit = '0' if toggle else '1'
            sizeOfMorseBit2, indexOfNextBit2 = find_transmission_rate(indexOfNextBit2, bit, bits)
            tempHelp += 1

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
    for i in range(0, len(bits), transmissionRate):
        subString = bits[i:i + transmissionRate]  # from the current position of the index, until (:) the size of the transmissionRate ==> create a substring to check the bits
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
    i = 0

    while i < len(decodedString):
        # check for ones
        if dashMorse == decodedString[i:i + 3]:
            morseString += "-"
            i += 3
            continue
        elif dotMorse == decodedString[i]:
            morseString += "."
            i += 1
            continue

        # check for zeroes
        if pauseBetweenWords == decodedString[i:i + 7]:
            morseString += "   "
            i += 7
        elif pauseBetweenChars == decodedString[i:i + 3]:
            morseString += " "
            i += 3
        elif pauseBetweenSymbols == decodedString[i]:
            i += 1
    #########################################################################################
    # Until here I find the proper form of Morse code with dots and dashes. morseString contains the form with dots '.' and dashed '-'
    # print(morseString)
    return morseString


def decode_morse(morseCode):
    dotsDashes = ""
    decodedString = ""
    for index, symbol in enumerate(morseCode):
        if symbol != ' ':
            dotsDashes += symbol
        else:
            if dotsDashes == "":
                if morseCode[index - 1] == ' ' and morseCode[index + 1] == ' ':
                    decodedString += " "
                continue
            else:
                decodedString += MORSE_CODE[dotsDashes]
                dotsDashes = ""
    decodedString += MORSE_CODE[dotsDashes]

    return decodedString


if __name__ == "__main__":
    bits = "11111111111111100000000000000011111000001111100000111110000011111000000000000000111110000000000000000000000000000000000011111111111111100000111111111111111000001111100000111111111111111000000000000000111110000011111000001111111111111110000000000000001111100000111110000000000000001111111111111110000011111000001111111111111110000011111000000000000000111111111111111000001111100000111111111111111000000000000000000000000000000000001111111111111110000011111000001111100000111110000000000000001111100000111111111111111000001111100000000000000011111111111111100000111111111111111000001111111111111110000000000000001111100000111111111111111000001111111111111110000000000000001111111111111110000011111000000000000000000000000000000000001111100000111110000011111111111111100000111110000000000000001111111111111110000011111111111111100000111111111111111000000000000000111111111111111000001111100000111110000011111111111111100000000000000000000000000000000000111110000011111111111111100000111111111111111000001111111111111110000000000000001111100000111110000011111111111111100000000000000011111111111111100000111111111111111000000000000000111110000011111111111111100000111111111111111000001111100000000000000011111000001111100000111110000000000000000000000000000000000011111111111111100000111111111111111000001111111111111110000000000000001111100000111110000011111000001111111111111110000000000000001111100000000000000011111000001111111111111110000011111000000000000000000000000000000000001111111111111110000000000000001111100000111110000011111000001111100000000000000011111000000000000000000000000000000000001111100000111111111111111000001111100000111110000000000000001111100000111111111111111000000000000000111111111111111000001111111111111110000011111000001111100000000000000011111111111111100000111110000011111111111111100000111111111111111000000000000000000000000000000000001111111111111110000011111000001111100000000000000011111111111111100000111111111111111000001111111111111110000000000000001111111111111110000011111111111111100000111110000000000000001111100000111111111111111000001111100000111111111111111000001111100000111111111111111"
    # bits = "111000111"
    morseStr = decode_bits(bits)

    humanString = decode_morse(morseStr)

    print("The human string is: {0}".format(humanString))
