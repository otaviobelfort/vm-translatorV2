# vm-translator

## Teste Execução

```
python3 main.py 07/MemoryAccess/BasicTest -b
python VMTranslator.py 07/MemoryAccess/BasicTest

```



notion: https://www.notion.so/Projeto-do-tradutor-63ab6e1d78f84f0287ee525aad41352d


```
func (code *CodeWriter) WritePush(seg string, index int) {
	switch seg {
	case "constant":
		code.write(fmt.Sprintf("@%d // push %s %d", index, seg, index))
		code.write("D=A")
		code.write("@SP")
		code.write("A=M")
		code.write("M=D")
		code.write("@SP")
		code.write("M=M+1")

```
