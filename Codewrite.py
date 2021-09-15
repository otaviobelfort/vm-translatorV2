class Codewrite:

    def __init__ (self, output_file):

        self.output = open(output_file, "w")
        self.module_name = "Bar"
        # count ++
        self.count_1 = 0
        self.count_2 = 0
        self.count_3 = 0
        self.count_4 = 0
        
    def write(self, mgs):
        print("{}".format(mgs), file=self.output)

    def segmentPointer(self, segment, index):
        if(segment == "local"): 
            return "LCL"
        elif(segment == "argument"): 
            return "ARG"
        elif(segment in ["this", "that"]): 
            return segment.upper()
        elif(segment == "temp"): 
            return "R{}".format(5+int(index))
        elif(segment == "pointer"): 
            return "R{}".format(3+int(index))
        elif(segment == "static"): 
            return "{}.{}".format(self.moduleName, index)
        else:
            return 'ERROR'
    
    def writeInit(self):
        self.write("@256")
        self.write("D=A")
        self.write("@SP")
        self.write("M=D")
        self.writeCall("Sys.init", 0)

    def writeBinary(self):
        self.write("@SP")
        self.write("AM=M-1")
        self.write("D=M")
        self.write("A=A-1")

    def writeUnary(self):
        self.write("@SP")
        self.write("A=M")
        self.write("A=A-1")
# --------------------------------------
    def writeArithmeticAdd(self):
        self.writeBinary()
        self.write("M=D+M")

    def writeArithmeticSub(self):
        self.writeBinary()
        self.write("M=M-D")

    def writeArithmeticAnd(self):
        self.writeBinary()
        self.write("M=D&M")
    
    def writeArithmeticOr(self):
        self.writeBinary()
        self.write("M=D|M")  

    def writeArithmeticNeg(self):
        self.writeUnary()
        self.write("M=-M") 

    def writeArithmeticNot(self):
        self.writeUnary()
        self.write("M=!M")
    
    def writeArithmeticGt(self):
        self.write("@SP")
        self.write("AM=M-1")
        self.write("D=M")
        self.write("A=A-1")
        self.write("D=M-D")

        self.write("@GT{}".format(self.count_1))
        self.write("D;JGT")
        self.write("@SP")
        self.write("A=M-1")
        self.write("M=0")

        self.write("@GTSTACK{}".format(self.count_1))
        self.write("0;JMP")
        self.write("(GT{})".format(self.count_1))
        self.write("@SP")
        self.write("A=M-1")
        self.write("M=-1")
        self.write("(GTSTACK{})".format(self.count_1))
        self.count_1 +=1 
             
    def writeArithmeticEq(self):
        self.write("@SP")
        self.write("AM=M-1")
        self.write("D=M")
        self.write("A=A-1")
        self.write("D=M-D")

        self.write("@EQ{}".format(self.count_2))
        self.write("D;JEQ")
        self.write("@SP")
        self.write("A=M-1")
        self.write("M=0")

        self.write("@EQSTACK{}".format(self.count_2))
        self.write("0;JMP")
        self.write("(EQ{})".format(self.count_2))
        self.write("@SP")
        self.write("A=M-1")
        self.write("M=-1")
        self.write("(EQSTACK{})".format(self.count_2))
        self.count_2 += 1

    def writeArithmeticLt(self):
        self.write("@SP")
        self.write("AM=M-1")
        self.write("D=M")
        self.write("A=A-1")
        self.write("D=M-D")

        self.write("@LT{}".format(self.count_3))
        self.write("D;JLT")
        self.write("@SP")
        self.write("A=M-1")
        self.write("M=0")

        self.write("@LTSTACK{}".format(self.count_3))
        self.write("0;JMP")
        self.write("(LT{})".format(self.count_3))
        self.write("@SP")
        self.write("A=M-1")
        self.write("M=-1")
        self.write("(LTSTACK{})".format(self.count_3))
        self.count_3 += 1
# --------------------------------------


    def writeArithmetic (self, command):

        if(command == "add"):
            self.writeArithmeticAdd()
        elif(command == "sub"):
            self.writeArithmeticSub()
        elif (command == "and"):
            self.writeArithmeticAnd()
        elif (command == "or"):
            self.writeArithmeticOr()
        elif(command == "neg"):
            self.writeArithmeticNeg()
        elif (command == "not"):
            self.writeArithmeticNot()
        elif (command == "gt"):
            self.writeArithmeticGt()
        elif (command == "eq"):
            self.writeArithmeticEq()
        elif (command == "lt"):
            self.writeArithmeticLt()
        else:
            pass
            
    
    def writePush(self, segment, index):

        if (segment == "constant"):
            self.write("@{} // push constant {}".format(index, index))
            self.write("D=A")
            self.write("@SP")
            self.write("A=M")
            self.write("M=D")
            self.write("@SP")
            self.write("M=M+1")
        elif (segment in ["local", "argument", "this", "that"]):
            self.write("@{} // push {} {}".format(self.segmentPointer(segment, index), segment, index))
            self.write("D=M")
            self.write("@{}".format(index))
            self.write("A=D+A")
            self.write("D=M")
            self.write("@SP")
            self.write("A=M")
            self.write("M=D")
            self.write("@SP")
            self.write("M=M+1")

        elif(segment in ["temp", "pointer", "static"]):

                self.write("@{} // push {}  {}".format(self.segmentPointer(segment, index), segment, index))
                self.write("D=M")
                self.write("@SP")
                self.write("A=M")
                self.write("M=D")
                self.write("@SP")
                self.write("M=M+1")
    
    def writePop(self, segment, index):
        if (segment in ["static", "temp", "pointer"]):
            self.write("@SP // pop {} {}".format(segment, index))
            self.write("M=M-1")
            self.write("A=M")
            self.write("D=M")
            self.write("@{}".format(self.segmentPointer(segment, index)))
            self.write("M=D")
        elif(segment in ["local", "argument", "this", "that"]):
            self.write("@{} // pop {} {}".format(self.segmentPointer(segment, index), segment, index))
            self.write("D=M")

            self.write("@{}".format(index))
            self.write("D=D+A")
            self.write("@R13")
            self.write("M=D")
            self.write("@SP")
            self.write("M=M-1")
            self.write("A=M")
            self.write("D=M")
            self.write("@R13")
            self.write("A=M")
            self.write("M=D")
    
    def writeIf(self, label):
        self.write("@SP")
        self.write("AM=M-1")
        self.write("D=M")
        self.write("M=0")
        self.write("@{}".format(label))
        self.write("D;JNE")

    def writeLabel(self, name):
        self.write("({})".format(name))

    def writeGoto(self, label):
        self.write("@{}".format(label))
        self.write("0;JMP")

    def writeFunction(self, funcName, n):
        loop = "{}_INIT_LOCALS_LOOP".format(funcName)
        endLoop = "{}_INIT_LOCALS_END".format(funcName)

        self.write("({})".format(funcName))
        self.write("@{}".format(n))
        self.write("D=A")
        self.write("@R13")
        self.write("M=D")
        self.write("({})".format(loop))
        self.write("@{}".format(endLoop))
        self.write("D;JEQ")
        self.write("@0")
        self.write("D=A")
        self.write("@SP")
        self.write("A=M")
        self.write("M=D")
        self.write("@SP")
        self.write("M=M+1")
        self.write("@R13")
        self.write("MD=M-1")
        self.write("@{}".format(loop))
        self.write("0;JMP")
        self.write("({})".format(endLoop))

    def writeFramePush(self, value):
        self.write("@{}".format(value))
        self.write("D=M")
        self.write("@SP")
        self.write("A=M")
        self.write("M=D")
        self.write("@SP")
        self.write("M=M+1")

    def writeCall(self, funcName, n):

        returnAddres = "{}_RETURN_{}".format(funcName, self.count_4)
        self.count_4 += 1

        self.write("@{}".format(returnAddres))
        self.write("D=A")
        self.write("@SP")
        self.write("A=M")
        self.write("M=D")
        self.write("@SP")
        self.write("M=M+1")

        self.writeFramePush("LCL")
        self.writeFramePush("ARG")
        self.writeFramePush("THIS")
        self.writeFramePush("THAT")

        self.write("@{}".format(n))
        self.write("D=A")
        self.write("@5")
        self.write("D=D+A")
        self.write("@SP")
        self.write("D=M-D")
        self.write("@ARG")
        self.write("M=D")

        self.write("@SP")
        self.write("D=M")
        self.write("@LCL")
        self.write("M=D")

        self.writeGoto(funcName)

        self.write("({})".format(returnAddres))


    def writeReturn(self):
        self.write("@LCL")
        self.write("D=M")

        self.write("@R13")
        self.write("M=D")

        self.write("@5")
        self.write("A=D-A")
        self.write("D=M")
        self.write("@R14")
        self.write("M=D")

        self.write("@SP")
        self.write("AM=M-1")
        self.write("D=M")
        self.write("@ARG")
        self.write("A=M")
        self.write("M=D")

        self.write("D=A")
        self.write("@SP")
        self.write("M=D+1")

        self.write("@R13")
        self.write("AM=M-1")
        self.write("D=M")
        self.write("@THAT")
        self.write("M=D")

        self.write("@R13")
        self.write("AM=M-1")
        self.write("D=M")
        self.write("@THIS")
        self.write("M=D")

        self.write("@R13")
        self.write("AM=M-1")
        self.write("D=M")
        self.write("@ARG")
        self.write("M=D")

        self.write("@R13")
        self.write("AM=M-1")
        self.write("D=M")
        self.write("@LCL")
        self.write("M=D")

        self.write("@R14")
        self.write("A=M")
        self.write("0;JMP")


    def close(self):
        self.output.close()
    

        




        
