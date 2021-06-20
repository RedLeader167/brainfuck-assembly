import sys, re

if len(sys.argv) < 3:
    print('Usage: python basm.py <input file> <output file>')
    exit()

print('brainfuck!assembly version 1.0')

basm = open(sys.argv[1]).read()
basm = basm.replace('\t', ' ')

finalbppc = 'bf/bf!asm v1\n'
finalbpp = ''

funcmode = 0
funcDic = {}
funcname = ''

lines = basm.split('\n')

def addv(text):
    global funcmode
    global funcDic
    global finalbpp
    global funcname
    
    if funcmode == 0:
        finalbpp += text
    elif funcmode == 1:
        funcDic[funcname] += text

for line in lines:
    asm_split = re.split(" |, |\(|\)", line)
    args = []
    for i in range (len(asm_split)):
        if (asm_split[i] != ""):
            args.append(asm_split[i])
    # print(args)
    if len(args) > 0:
        if args[0] == 'inc':
            addv("+")
        elif args[0] == 'dec':
            addv("-")
        elif args[0] == 'mov':
            if len(args) > 1:
                if args[1].isdigit():
                    addv("+[-]")
                    for i__ in range(int(args[1])):
                        addv("+")
                else:
                    print('Compiler error: mov instruction argument is invalid and not int.')
                    exit()
            else:
                print('Compiler error: mov instruction without int passed.')
                exit()
        elif args[0] == 'mvc':
            if len(args) > 1:
                addv("+[-]")
                for i__ in range(ord(args[1][0])):
                    addv("+")
            else:
                print('Compiler error: mvc instruction without char passed.')
                exit()
        elif args[0] == 'add':
            if len(args) > 1:
                if args[1].isdigit():
                    for i__ in range(int(args[1])):
                        addv("+")
                else:
                    print('Compiler error: add instruction argument is invalid and not int.')
                    exit()
            else:
                print('Compiler error: add instruction without int passed.')
                exit()
        elif args[0] == 'sub':
            if len(args) > 1:
                if args[1].isdigit():
                    for i__ in range(int(args[1])):
                        addv("-")
                else:
                    print('Compiler error: sub instruction argument is invalid and not int.')
                    exit()
            else:
                print('Compiler error: sub instruction without int passed.')
                exit()
        elif args[0] == 'pcc':
            addv(".")
        elif args[0].startswith(';'):
            pass
        elif args[0] == 'hlt':
            pass
        elif args[0] == 'mpr':
            addv(">")
        elif args[0] == 'mpl':
            addv("<")
        elif args[0] == 'clp':
            addv("[")
        elif args[0] == 'elp':
            addv("]")
        elif args[0] == 'gcc':
            addv(",")
        elif args[0] == 'function':
            if len(args) > 1:
                if funcmode == 0:
                    funcmode = 1
                    funcname = args[1]
                    funcDic[args[1]] = ""
                else:
                    print('Compiler error: function already defining.')
                    exit()
            else:
                print('Compiler error: function instruction without string passed.')
                exit()
        elif args[0] == 'endfunc':
            if funcmode == 1:
                funcmode = 0
                funcname = ''
            else:
                print('Compiler error: function not defining.')
                exit()
        elif args[0] == 'call':
            if len(args) > 1:
                if funcmode == 1:
                    if args[1] == funcname:
                        print('Compiler error: recursion not allowed.')
                        exit()
                addv(funcDic[args[1]])
            else:
                print('Compiler error: call instruction without string passed.')
                exit()
        else:
            print('Compiler error: instruction ' + args[0] + ' is not a valid instruction.')
            exit()

open(sys.argv[2], 'w').write(finalbppc + finalbpp)

print('Compiled successfully, size is ' + str(len(finalbpp)) + ' bytes, total size is ' + str(len(finalbppc + finalbpp)) + '.')