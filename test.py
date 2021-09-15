
from Codewrite import Codewrite
import sys
import os
import Codewrite

inputfile= sys.argv[1]
inputfile = inputfile.strip()
print("inputfile: ")

print(inputfile)

outputfile = inputfile.replace("vm","asm")
print(outputfile)

Codewrite.Codewrite(outputfile)
