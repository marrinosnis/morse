# Morse Decoder
![Tests](https://github.com/marrinosnis/morse/actions/workflows/runTests.yaml/badge.svg)


## Overview
This project was created from 2 parts of an exercise in CodeWars website about the decode process of the morse code.\
The first part is implemented in `C++` and can be found [here](https://www.codewars.com/kata/54b724efac3d5402db00065e/cpp).\
The second part, which is a continuation of the first part is implemented in `Python` and can be found [here](https://www.codewars.com/kata/54b72c16cd7f5154e9000457/python). \

> [!NOTE]  
> **_Each of the 2 parts that are combined in this project, has passed all the required tests the CoderWars\
> site needs in order to make the solution acceptable. In order to combine the 2 solutions, a refactor has been \
> applied. Given that, the final combination outcome will differ from the independent parts of code._**

> [!NOTE]  
> Please make sure that you have read and **understand** the definition and rules of each part in order to \
> have a full sight of the project solution.

## Prerequisites
In order to be able to run the main `morse.py` file, you should have installed the `Python 3.10.x` version \
and the `C++ 14` version `(-std=c++14)`. These versions are necessary in order to execute the script file \
`build.sh` which is responsible for creating the custom Python module. This script file can found in \
the following path: 
>*src/services/cppToPythonModule*

There are the declarations of the versions for the Python and C++.

To check the versions that you have installed on your machine: \
For python
> python3 --version

For C++:
>  g++ --version

> [!NOTE]  
> Also make sure that you have installed the `g++` compiler instead of `gcc`. This might be a minor but very \
> important notice. With the `gcc` compiler there might occur some mulfunctioning

## Structure - Flow - Steps of procedure
**1**: The main file `morse.py` where the binary data are read from the file `binaryMorseCode.txt` and all the \
modules-functions and classes are called to print the final result. It can be found to the following path:
>*src/main/morse.py*

**2**: The conversion from binary structured string to morse code format string with dots-dashes\
is implemented in python. The functions can be found to the following path: 
>*src/services/BinaryCodeToMorseCode*

- *2.1* The `bitsToMorseCode.py` handles all the requirements of the 2nd part that can be found [here](https://www.codewars.com/kata/54b72c16cd7f5154e9000457/python), \
as for the clarification and removal of the transmission rate that a binary string may have. 
- *2.2* Once this is done, then `convertBinaryToMorseSymbols.py` is called, to create and return \
the final morse code formatted string that has been created with the original binary format.

**3**: Having the correct morse code string format, without any additional _noise_ from the transmission rate, \
a custom module is used to generate the final human-readable string. The custom module is written \
in a simple `C++` class, and using the opensource library [pybind11](https://github.com/pybind/pybind11) to create a shared object (`.so`) \
which will be included as a python module in the main `morse.py` file.

**4**: The final outcome that will be printed in the console will be the results of each step, e.g.:
```
The transmissionRate of this string is:  1
The proper bits representation is 1011101010001000101110001011101000111010000000111011100011101110111000101110100010101000100010101110111010111000111010111010001110111011100011101010001

The final morse code form is: .-.. . .- .-. -.   -- --- .-. ... . ..--.- -.-. --- -.. .

The respective human readable string is: LEARN MORSE_CODE
```
If you want to test your own binary string with or without transmission rate, just got at the `morse.py` file and at the \
line 11: `morseString = bitsToMorseCode.convertBitsToDotsDashes(binaryMorseCode[4])` in the functio \
`convertBitsToDotDashes()`, remove the current parameter and put your own binary morse code. Make sure the \
type is `string - str`.

## Tests
