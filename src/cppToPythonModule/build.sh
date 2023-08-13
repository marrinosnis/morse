# it creates the morse.so module, at the parent folder
g++ -shared -fPIC -std=c++14 -I./pybind11/include/ `python3.10 -m pybind11 --includes` ../cppMorseDecoder/MorseDecoder.cpp morseModule.cpp -o ../morseModule.so `python3.10-config --ldflags`

#copy the shared object and at the tests folder, for testing purposes
cp ../morseModule.so ../../tests/