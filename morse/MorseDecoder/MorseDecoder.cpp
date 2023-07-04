#include <iostream>
#include <string>
#include "MorseDecoder.h"
#include "MorseDictionary.h"

std::string MorseDecoder::decodeMorse(std::string morseCode){
    //morseCode = "          .-.. .- --.. -.--   -.. --- --. .-.-.-   "
    //morseCode = "       .       ";
    
    std::string decoded {};
    std::string dotsDashes {};
    int sizeOfString = morseCode.size();

    morseCode.erase(0, morseCode.find_first_not_of(" ")); //remove any leading space, up until the first dot '.' or dash '-'
    morseCode.erase(morseCode.find_last_not_of(" ") + 1); //remove any trailing space, from the last dot '.' or dash '-' untill the end of the string

    for (int index = 0; index < sizeOfString; index++){
      
      while( (morseCode[index] != ' ' && index < sizeOfString) ){
        dotsDashes += morseCode[index];
        index++;
      } //if it goes out from the while, that means I reach to a space. Now I need to check the size of the space. If it is 1, that means 
        //I just need to decode the current part of dots and dashes, and continue to the other dots and dashes
      
      decoded += MORSE_CODE[dotsDashes];
      dotsDashes = "";
      
      if (morseCode[index+1] == ' ' && morseCode[index+2] == ' ') { //here is the fucking problem
        decoded += " ";
        index += 2;
      }

    }
  
  return decoded;

}