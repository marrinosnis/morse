g++ -shared -fPIC -std=c++14 -I./pybind11/include/ `python3.10 -m pybind11 --includes` ../MorseDecoder/MorseDecoder.cpp morseModule.cpp -o ../morse.so `python3.10-config --ldflags`
                         # it creates the mymodule.so module, at the previous path folder, because of that ^
