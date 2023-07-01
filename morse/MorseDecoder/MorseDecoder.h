#pragma once
#include <string>

class MorseDecoder{
public:
    MorseDecoder(){}
    std::string decodeMorse(std::string morseCode);
    ~MorseDecoder(){}

};