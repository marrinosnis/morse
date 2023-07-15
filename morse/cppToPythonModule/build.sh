g++ -shared -fPIC -std=c++14 -I./pybind11/include/ `python3.10 -m pybind11 --includes` ../cppMorseDecoder/MorseDecoder.cpp morseModule.cpp -o ../morse.so `python3.10-config --ldflags`
                         # it creates the morse.so module, at the parent folder
