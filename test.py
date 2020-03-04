import math
import os
import sys

import requests

print (sys.version)

test = "Test"


print(sys.executable)

r = requests.get('http://kolks.nl')
print(r.status_code)

name = input ("your name")
print ("Hello", name)