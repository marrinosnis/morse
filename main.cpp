#include <iostream>
#include <string>
#include <map>
#include "morse/MorseDecoder.h"

int main(int argc, char* argv[]){

  MorseDecoder md;

  std::string morseString = ".... . -.--   .--- ..- -.. .";
  std::string humanString {};

  humanString = md.decodeMorse(morseString);

  std::cout<<"The text is:\n" << humanString << '\n';


  return 0;
}

