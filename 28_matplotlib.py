# 28_matplotlib.py

# matplotlib provide the creation of graphs -> pip install matplotlib
# it is also automatically installed when scikit-learn is installed -> pip install scikit-learn
# NOTE: google python modules
#  https://realpython.com/python-modules-packages/
#  https://docs.python.org/3/tutorial/modules.html
# What's the difference between a Python module and a Python package?
#   https://stackoverflow.com/questions/7948494/whats-the-difference-between-a-python-module-and-a-python-package
# requests, later presented -> pip install requests
# wxPython - used to graphic interface for python programs -  
# SciPy - SciPy.org - mathematics scientific calculations module
# pygame - for games
# sqlAlchemy module - used to make connections to databases -- 
# google python 

import matplotlib.pyplot as plt
import numpy as np


x = [1,2,3,4]
y = [1500,1200,1100,1800]

print(x)
print(y)

plt.plot(x,y)
plt.show()

