# brainfuck!assembly
Assembly for Brainfuck

Uses special assembler language, compiles into brainfuck

# Instructions:

add #	: adds # to cell

sub #	: subs # from cell

mov #	: sets # to cell

mvc C : sets character to cell

inc		: increments cell

dec		: decrements cell

mpr		: moves pointer to right

mpl		: moves pointer to left

pcc		: prints cell as character

gcc		: gets the character

clp   : starts loop

elp   : ends loop

function String  : creates function with name

endfunc          : ends function

call String      : calls function

clm # : moves cell value from current to cell with offset # (can be negative)

clc #, 2# : copies cell value to cell with offset #, cell 2# will be nullified

# How to use:

Compiling: python asm.py inputFile.basm outputFile.bf
