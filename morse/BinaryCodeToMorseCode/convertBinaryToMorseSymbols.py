
def createProperMorseCodeString(binaryString):
    morseString = ""
    dashMorse = "111"
    dotMorse = "1"
    pauseBetweenWords = "0000000"
    pauseBetweenChars = "000"
    pauseBetweenSymbols = "0"
    i = 0

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
