#include "morse.h"
#include "morseDictionary.h"

std::string MorseDecoder::decodeMorse(std::string morseCode){
  int counterSpace {0};
  std::string decoded {};
  std::string word {};

    for(int i=0; i< morseCode.size(); i++ ){
         if( morseCode[i] == ' ' ) //when I found a space, an action should be taken
        {
          counterSpace++;
          //if the counterSpace is equal to 3, that means I should add 1 'human' space.
          //Because of any spaces before or after the code should be ignored, when I reach at 3 spaces in total I check if: 
          
          //from the current position, any of the 3 previous positions have '.' or '-'.If not, that means it's a 'human' space
          //before the basic phrase, and should be ignored. 
          
          //To check if there is any 'human' space after the basic phrase, that should be ignored,
          //I did that: based on the instructions it's not possible to have 4 space in sequence at the code, 
          //because 3 spaces are the limit to represent a human space, so a 4th one cannot be represented. 
          //With that in mind, if 3 spaces in code reached, and if the character at the next position is NOT '.' or '-', that
          //means an extra redudant space is there, and the code should ignore it.
          
          //But if all the above mentioned rules are TRUE, as they impement below, then a 'human' space should be add.
          
          if(counterSpace == 3 && ( (morseCode[i-1] == '.' || morseCode[i-1] == '-') || (morseCode[i-2] == '.' || morseCode[i-2] == '-') || (morseCode[i-3] == '.' || morseCode[i-3] == '-')) && (morseCode[i+1] == '.' || morseCode[i+1] == '-') ) 
          {
            decoded += " ";
          } 
          
          else // if there were not 3 spaces, that means there is 1, and the 'word' variables should be decoded based
          {    // on the Morse Table
            decoded += MORSE_CODE[word];
            word = "";
          }  
        }
        
        else //if the current check is not space, it is added to the 'word' variable, that when a space occur, it will be decode.
        {
          counterSpace = 0;
          word +=morseCode[i];  //store each symbol at the 'word' variable, to perform the conversion when a space occur
        }
    }
  
   decoded += MORSE_CODE[word]; //a last one conversation is added, because when it reaches at the last symbol, '.' or '-', 
                                //there is no space after that, so the proper part conversion code isn't execute. That's why 
                                //it is added here.
    return decoded;
}