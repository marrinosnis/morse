#include "../MorseDecoder/MorseDecoder.h"
#include <pybind11/pybind11.h>

namespace py = pybind11;

PYBIND11_MODULE(morse, m){  //'morse' is the shared object that is created and will be imported in the python file as 'morse' module
    m.doc() = "Create a Python module for morseDecoder";
    
    py::class_<MorseDecoder>(m, "MorseDecoderString")  // 'MorseDecoderString' is the name of the class that will be used at the python file. So I can have different name for the .cpp class
      .def(py::init())
      .def("decodeMorse", &MorseDecoder::decodeMorse); // 'decodeMorse' is the function that will be used in python file. The name that I declare there is used at python
}