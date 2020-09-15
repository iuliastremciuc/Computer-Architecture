"""
Number Bases
-------------

It's the 'language' that a number is written down in.

Douze == Twelve
1100 == 12

Base 2: binary
Base 8: octal (rarely used)
Base 10: decimal (what we know from grade school, regular boring ol numbers)
Base 16: hexademical, "hex"
Base 64: bace 64


base 10

+-----1000's place
|+----100's place
||+---10's place
|||+--1's place
||||
abcd
1234

1 1000
2 100s
3 10s
1 1s

1234 == 1 * 1000 + 2 * 100 + 3 * 10 + 4 * 1



base 2 (binary)

+-----8's place 2^3
|+----4's place 2^2
||+---2's place 2^1
|||+--1's place 2^0
||||
abcd


0011

0011 binery == 0 * 8 + 0 * 4 + 1 * 2 + 1 * 1 == 3 decimal
^
binary digits ('bit')

8 bits == "byte"
4 bits == "nybble"

To specify the base in code:

Prefix
------
[none] decimal
0b  binery
0x  hex
0o  octal

yello
#ffff00     #ffffff     #000000
red         green       blue

255         255         0           decimal base 10
ff          ff          00          hex     base 16
11111111    11111111    00000000    binary  base 2

"""



# These all mean the same thing:
#   Index into the memory array
#   Address
#   Location
#   Pointer

memory = [
	1,  # PRINT_BEEJ  Address 0
	3,  # SAVE_REG R1,37
	1,
	37,
	4,  # PRINT_REG R1
	1,
	2,  # HALT
]

registers = [0] * 8  # R0-R7

# "Variables" in hardware. Known as "registers".
# There are a fixed number of registers
# They have fixed names
#  R0, R1, R2, ... , R6, R7

pc = 0  # Program Counter, address of the currently-executing instuction

running = True

while running:
	ir = memory[pc]  # Instruction Register, copy of the currently-executing instruction

	if ir == 1:  # PRINT_BEEJ
		print("Beej!")
		pc += 1

	elif ir == 2:
		running = False

	elif ir == 3:  # SAVE_REG
		reg_num = memory[pc + 1]
		value = memory[pc + 2]
		registers[reg_num] = value
		pc += 3

	elif ir == 4:  # PRINT_REG
		reg_num = memory[pc + 1]
		print(registers[reg_num])
		pc += 2

	else:
		print(f"Unknown instruction {b}")

