"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0
        self.running = True
    
    def ram_read(self, indx):
        return self.ram[indx]

    def ram_write(self, value, indx):

        self.ram[indx] = value


    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:
 
        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]

        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1
        print(sys.argv)
        if len(sys.argv) != 2:
            print("usage: ls8.py filename")
            sys.exit(1)

        try:
            with open(sys.argv[1]) as f:
                for line in f:
                    spliting = line.split('#')
                    v = spliting[0].strip()

                    if v == '':
                        continue

                    try:
                        v = int(v, 2)
                    except ValueError:
                        print(f"Invalid number '{v}'")
                        sys.exit(1)

                    self.ram[address] = v
                    address += 1

        except FileNotFoundError:
            print(f"File not found: {sys.argv[1]}")
            sys.exit(2)


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""
        # reg_a = self.ram_read(self.pc + 1)
        # reg_b = self.ram_read(self.pc + 2)

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        
        elif op == "MUL":
            multy = self.reg[reg_a] * self.reg[reg_b]
            self.reg[reg_a] = multy
            self.pc += 3
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        HLT = 0b00000001
        PRN = 0b01000111
        LDI = 0b10000010
        MUL = 0b10100010
        PUSH = 0b01000101
        POP = 0b01000110
        SP = 7
        self.reg[SP] = 0xF4


        while self.running:

            ir = self.ram_read(self.pc)
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)
        
            if ir == HLT:    # HLT   1
                self.running = False

            elif ir == PRN:  # PRN   71
                # reg_num = self.ram_read(self.pc + 1)

                print(self.reg[operand_a])
                self.pc += 2

            elif ir == LDI: # LDI    130
                self.reg[operand_a] = operand_b
                self.pc += 3

            elif ir == MUL:  # MUL
                multy = self.reg[operand_a] * self.reg[operand_b]
                self.reg[operand_a] = multy
                self.pc += 3
            
            elif ir == PUSH:  # PUSH
                self.reg[SP] -= 1

                reg_num = self.ram[self.pc + 1]

                value = self.reg[reg_num]

                top_of_stac_ad = self.reg[SP]

                self.ram[top_of_stac_ad] = value

                self.pc += 2

            elif ir == POP:  # POP
                reg_num = self.ram[self.pc + 1]

                top_of_stac_ad = self.reg[SP]

                value = self.ram[top_of_stac_ad]

                self.reg[reg_num] = value

                self.reg[SP] += 1

                self.pc += 2

            





        
