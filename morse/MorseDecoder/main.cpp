#include <iostream>
#include "MorseDecoder.h"
#include <string>
#include <fstream>

int main() {
    
    
    MorseDecoder md;
    std::string  text = "marinos";

    text = md.decodeMorse(text);
    std::cout<<"The string is:\n" << text << '\n';





    
    return 0;
}