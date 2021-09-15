import pandas as np
from glob import glob
import os
import sys

dir = '../vm-translator/vazio/'
import os 

x = os.path.isdir(dir)
print("x",x)

list_file = sorted(glob(r'../vm-translator/vazio/*.jack'))
#list_file = list_file[0].split("/")[-1]


if (list_file is []): 
    print("diretório vazio")
else:
    print(list_file)

inp = sys.argv
print(inp)

#print(list_file is True)

