#include <iostream>
#include <string>
#include "MorseDecoder.h"
#include "MorseDictionary.h"
#include <fstream>

std::string MorseDecoder::decodeMorse(std::string morseCode){
    std::string decodedString {};
    std::string dotsDashes {};
    std::string morseCodeNoSpaces {};

    morseCode.erase(0, morseCode.find_first_not_of(" ")); //remove any leading space, up until the first dot '.' or dash '-'
    morseCode.erase(morseCode.find_last_not_of(" ") + 1); //remove any trailing space, from the last dot '.' or dash '-' until the end of the string
    morseCodeNoSpaces = morseCode; //when I used the morseCode string, the removed trailing spaces were still accessible from the 28th line
    int sizeOfString = morseCodeNoSpaces.size();

    // loop through the Morse Code, to produce a human readable string 
     for (int index = 0; index < sizeOfString; index++){
      
      while( (morseCodeNoSpaces[index] != ' ' && index < sizeOfString) ){
        dotsDashes += morseCodeNoSpaces[index];
        index++;
      }

      decodedString += MORSE_CODE[dotsDashes];
      dotsDashes = "";
      
      if ( morseCodeNoSpaces[index+1] == ' ' && morseCodeNoSpaces[index+2] == ' ') {
        decodedString += " ";
        index += 2;
      }
    }

    return decodedString;
}