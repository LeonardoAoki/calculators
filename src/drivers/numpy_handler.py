import numpy
from typing import List
from .interfaces.driver_handler_interface import DriverhandlerInterface

class NumpyHandler(DriverhandlerInterface):
    def __init__(self):
        self.__np = numpy

    def standard_derivation(self, numbers: List[float]) -> float:
        return self.__np.std(numbers)
    
    def variance(self, numbers: List[float]) -> float:
        return self.__np.var(numbers)