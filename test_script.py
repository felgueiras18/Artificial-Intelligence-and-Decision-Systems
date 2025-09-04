#test script to make sure all dependencies are correctly installed

import sys
import numpy as np

print("Python executable:", sys.executable)
print("Python version:", sys.version)
print("NumPy location:", np.__file__)
print("NumPy version:", np.__version__)