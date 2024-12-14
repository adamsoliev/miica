#! /usr/bin/python3

RAM = bytearray(640)  # data memory | each 4002 RAM chip consists of 4 of 40-byte banks

ROM = bytearray(4096) # program memory | each 4001 ROM chip is 256-byte

PROGRAM_COUNTER = bytearray(12)         # pc
STACK_REGISTERS = [bytearray(12)] * 3   # stack
INDEX_REGISTERS = [bytearray(4)] * 16   # registers
ACCUMULATOR = bytearray(4)              
TEMPORARY_REGISTER = bytearray(4)       # carry?
INSTRUCTION_REGISTER = bytearray(8)     

from enum import Enum

class InstructionSet(Enum):
    # Data Transfer Instructions
    LD = 0b1010    # Load register to accumulator
    LDM = 0b1101  # Load data to accumulator
    IAC = 0b1111  # Increment accumulator
    TCC = 0b1111  # Transfer carry to accumulator and clear carry
    DAC = 0b1111  # Decrement accumulator
    TCS = 0b1111  # Transfer carry subtract and clear carry
    STC = 0b1111  # Set carry
    DAA = 0b1111  # Decimal adjust accumulator

    # Fetch
    FIM = 0b0010  # Fetch immediate data to register pair
    FIN = 0b0011  # Fetch indirect from ROM

    # Arithmetic Instructions
    ADD = 0b1000  # Add register to accumulator
    SUB = 0b1001  # Subtract register from accumulator
    XCH = 0b1011  # Exchange accumulator with register

    # Logical Instructions
    CMC = 0b1111  # Complement carry
    CMA = 0b1111  # Complement accumulator
    CLB = 0b1111  # Clear both accumulator and carry
    CLC = 0b1111  # Clear carry
    RAL = 0b1111  # Rotate left (accumulator and carry)
    RAR = 0b1111  # Rotate right (accumulator and carry)

    # Branch Instructions
    JIN = 0b0011  # Jump indirect
    JUN = 0b0100  # Jump unconditional
    JMS = 0b0101  # Jump to subroutine
    JCN = 0b0001  # Jump conditional
    ISZ = 0b0111  # Increment and skip if zero

    # Machine Control Instructions
    NOP = 0b0000  # No operation
    INC = 0b0110  # Increment register
    BBL = 0b1100  # Branch back and load

    # Other
    KBP = 0b1111  # Keyboard process
    DCL = 0b1111  # Designate group

    # I/O and RAM Instructions
    SRC = 0b0010
    WRM = 0b1110
    WMP = 0b1110
    WRR = 0b1110
    WPM = 0b1110
    WRO = 0b1110
    WR1 = 0b1110
    WR2 = 0b1110
    WR3 = 0b1110
    SBM = 0b1110
    RDM = 0b1110
    RDR = 0b1110
    ADM = 0b1110
    RD0 = 0b1110
    RD1 = 0b1110
    RD2 = 0b1110
    RD3 = 0b1110


def parse_assembly_file(filename):
    instructions = []
    with open(filename, 'r') as file:
        for line in file:
            if ':' not in line or not line.strip():
                continue
            bytes = line.split(':')[1].strip().split()
            i = 0
            while i < len(bytes):
                first_opr = int(bytes[i][0], 16)
                second_opa = int(bytes[i][1], 16) & 0b1
                if first_opr == 0b10:
                    if second_opa == 0:
                        instructions.append(InstructionSet.FIM)
                        i += 2
                    else:
                        instructions.append(InstructionSet.SRC)
                        i += 1
                elif first_opr in [0b1,0b100,0b101,0b111]:
                    instructions.append(InstructionSet(first_opr))
                    i += 2
                else:
                    if first_opr == 0b11:
                        if second_opa == 0:
                            instructions.append(InstructionSet.FIN)
                        else:
                            instructions.append(InstructionSet.JIN)
                    else:
                        instructions.append(InstructionSet(first_opr))
                    i += 1
    for instruction in instructions:
        print(instruction)


def fetch():
    return 

def decode(string):
    return

def execute(opcode, operands):
    return

if __name__ == "__main__":
    parse_assembly_file('sanity_test.asm')


# ------------------------------------------------------------------
# ------------------------------------------------------------------
# ------------------------------------------------------------------
'''
| address |             | storage |  status |
|   0-15  |  register 0 | 8 bytes | 2 bytes |
|  16-31  |  register 1 | 8 bytes | 2 bytes |
|  32-47  |  register 2 | 8 bytes | 2 bytes |
|  48-63  |  register 2 | 8 bytes | 2 bytes |

the above is a bank; RAM chips were arranged in up to 4 banks of up to 4 chips
'''