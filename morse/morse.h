#pragma once
#include <string>
#include <map>

class MorseDecoder{
public:
    MorseDecoder(){}
    std::string decodeMorse(std::string morseCode);
    ~MorseDecoder(){}
};