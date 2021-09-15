class Parser():

    def __init__(self, input_file):
        self.input_file = input_file
        self.file = open(input_file, "r")
        self.temp = self.file.readlines()
        self.tokens = []
        self.currTokenIndex = 0
        self.formLines()

    def formLines(self):
        for line in self.temp:
            self.tokens.append(line.replace("\n", ""))

    def hasMoreCommands(self):
        #state = self.currTokenIndex <= len(self.tokens)-1
        return self.currTokenIndex <= len(self.tokens)-1

    def advance(self):
        if (self.hasMoreCommands()):
            self.currTokenIndex += 1
    
    def currCommand(self):
        return self.tokens[self.currTokenIndex]

    def nextCommand(self):
        command = self.currCommand()
        list_cmd = command.split(" ")
        foo = list_cmd[0]
        if (command in ['add','sub','neg','eq','gt','lt','and','or','not']):
            return "Arithmetic"
        else:
            if   (foo == "pop"): 
                return "Pop"
            elif (foo == "push"): 
                return "Push"
            elif (foo == "call"): 
                return "Call"
            elif (foo == "function"): 
                return "Function"
            elif (foo == "return"): 
                return "Return"
            elif (foo == "label"): 
                return "Label"
            elif (foo == "goto"): 
                return "Goto"
            elif (foo == "if-goto"): 
                return "If"
            else : 
                return None
    
    def arg1(self):
        if(self.nextCommand() == "Arithmetic"):
            return self.currCommand()
        elif(self.nextCommand() == "Return"):
            return None
        else:
            return self.currCommand().split(" ")[1]
    
    def arg2(self):
        if(self.nextCommand() in ["Push", "Pop", "Function", "Call"]):
            return self.currCommand().split(" ")[2]
        else:
            return None

    









