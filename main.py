
import os
import sys
from Codewrite import Codewrite
from Parser import Parser

import Parser
import Codewrite

def isDirectory(path):
    dir = os.path.isdir(path)
    if dir:
        return True
    else:
        return False


def translate(path, code):
    while path.hasMoreCommands():
        type = path.nextCommand()
        #print("type: ",type)

        #type = Parser.Parser.hasMoreCommands()

        if (type == "Push"):
            code.writePush(path.arg2(), path.arg2())
            path.advance()
        elif (type == "Pop"):
            code.writePop(path.arg1(), path.arg2())
            path.advance()
        elif (type == "Arithmetic"):
            code.writeArithmetic(path.arg1())
            path.advance()

        elif(type == "Label"):
            code.writeLabel(path.arg1())
            path.advance()
        elif (type == "Goto"):
            code.writeGoto(path.arg1())
            path.advance()
        elif (type == "If"):
            code.writeIf(path.arg1())
            path.advance()

        elif (type == "Call"):
            code.writeCall(path.arg1(), path.arg2())
            path.advance()
        elif (type == "Return"):
            code.writeReturn()
            path.advance()
        elif (type == "Function"):
            code.writeFunction(path.arg1(), path.arg2())
            path.advance()
        else:
            print(path.currCommand())
            print('ERROR! \n write "{}" não implementado'.format(type))
            path.advance()

def main():
    input_file_dir = sys.argv[1]
    #input_file_dir = "vm-translator/08/FunctionCalls/FibonacciElement/Main.vm"
    vm_files = []

    print("-- teste --- input_file_dir:  ")
    print(input_file_dir)

    #isDirectory()
    if(os.path.isdir(input_file_dir)):
        list_dir = input_file_dir.split("/")
        output_file = list_dir[len(list_dir)-1]
        #output_file = "out_main"

        
        _, _, filenames = next(os.walk(input_file_dir))
        print("--- file names: ",filenames)


        for file in filenames:
            if(file.endswith(".vm")):
                vm_files.append("{}/{}".format(input_file_dir,file))

        #print( "file .asm: ","{}/{}.asm".format(input_file_dir, output_file))
        code = Codewrite.Codewrite("{}/{}.asm".format(input_file_dir, output_file))
        if(len(sys.argv) < 3):

            for vm_item in vm_files:
                path = Parser.Parser(vm_item)
      
                translate(path,code)

        else:
            if (sys.argv[2] == "-b"):
                code.writeInit()
                for vm_item in vm_files:
                    list_dir = vm_item.split("/")
                    output_file = list_dir[len(list_dir) - 1]
                    module_name = output_file.split(".")[0]

                    code.module_name = module_name
                    path = Parser.Parser(vm_item)
                    translate(path, code)

            else:
                print("error")

        code.close()

    else:
        list_dir = input_file_dir.split("/")
        output_file_name = input_file_dir.split(".")[0]

        output_file = list_dir[len(list_dir) - 1]
        #output_file = "out_main"
        #module_name = "out_main"
        module_name = output_file.split(".")[0]


        #code = codewrite.codewrite("{}.{}".format(output_file,"asm"))
        #code = codewrite("out_main.asm")
        code = Codewrite.Codewrite(output_file_name+".asm")

        code.module_name = module_name

        if (len(sys.argv) < 3):
            # print(inputFileOrDir)
            path = Parser.Parser(input_file_dir)
            translate(path, code)
            code.close()

        else:
            if(sys.argv[2] == "-b"):
                code.writeInit()
                path = Parser.Parser(input_file_dir)
                translate(path, code)
                code.close()
            else:
                print("ERROR!")


#if __name__ == '__main__':

main()
