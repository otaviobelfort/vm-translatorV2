@256
D=A
@SP
M=D
@Sys.init_RETURN_0
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@5
D=D+A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.init
0;JMP
(Sys.init_RETURN_0)
@LCL // pop local 0
D=M
@0
D=D+A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
@ARG // pop argument 2
D=M
@2
D=D+A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
@ARG // pop argument 1
D=M
@1
D=D+A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
@THIS // pop this 6
D=M
@6
D=D+A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
@THAT // pop that 5
D=M
@5
D=D+A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
@THAT // pop that 2
D=M
@2
D=D+A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
@SP // pop temp 6
M=M-1
A=M
D=M
@R11
M=D
@SP
AM=M-1
D=M
A=A-1
M=D+M
@SP
AM=M-1
D=M
A=A-1
M=M-D
@SP
AM=M-1
D=M
A=A-1
M=D+M
@SP
AM=M-1
D=M
A=A-1
M=M-D
@SP
AM=M-1
D=M
A=A-1
M=D+M
