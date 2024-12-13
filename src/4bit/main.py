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
    LD = (0b1010, None)    # Load register to accumulator
    LDM = (0b1101, None)    # Load data to accumulator
    CLB = (0b1111, 0b0000)  # Clear both accumulator and carry
    CLC = (0b1111, 0b0001)  # Clear carry
    IAC = (0b1111, 0b0010)  # Increment accumulator
    CMC = (0b1111, 0b0011)  # Complement carry
    CMA = (0b1111, 0b0100)  # Complement accumulator
    RAL = (0b1111, 0b0101)  # Rotate left (accumulator and carry)
    RAR = (0b1111, 0b0110)  # Rotate right (accumulator and carry)
    TCC = (0b1111, 0b0111)  # Transfer carry to accumulator and clear carry
    DAC = (0b1111, 0b1000)  # Decrement accumulator
    TCS = (0b1111, 0b1001)  # Transfer carry subtract and clear carry
    STC = (0b1111, 0b1010)  # Set carry
    DAA = (0b1111, 0b1011)  # Decimal adjust accumulator

    # Fetch
    FIM = (0b0010, 0b0000)    # Fetch immediate data to register pair
    FIN = (0b0011, 0b0000)    # Fetch indirect from ROM

    # Arithmetic Instructions
    ADD = (0b1000, None)    # Add register to accumulator
    SUB = (0b1001, None)    # Subtract register from accumulator
    XCH = (0b1011, None)    # Exchange accumulator with register

    # Logical Instructions
    CLC = (0b1111, 0b0001)  # Clear carry
    CMC = (0b1111, 0b0011)  # Complement carry
    CMA = (0b1111, 0b0100)  # Complement accumulator
    RAL = (0b1111, 0b0101)  # Rotate left through carry
    RAR = (0b1111, 0b0110)  # Rotate right through carry

    # Branch Instructions
    JIN = (0b0011, 0b0001)    # Jump indirect
    JUN = (0b0100, None)    # Jump unconditional
    JMS = (0b0101, None)    # Jump to subroutine
    JCN = (0b0001, None)    # Jump conditional
    ISZ = (0b0111, None)    # Increment and skip if zero

    # Machine Control Instructions
    NOP = (0b0000, None)    # No operation
    INC = (0b0110, None)    # Increment register
    BBL = (0b1100, None)    # Branch back and load

    # Other
    KBP = (0b1111, 0b1100)  # Keyboard process
    DCL = (0b1111, 0b1101)  # Designate group

    # I/O and RAM Instructions
    SRC = (0b0010, 0b0001)
    WRM = (0b1110, 0b0000)
    WMP = (0b1110, 0b0001)
    WRR = (0b1110, 0b0010)
    WPM = (0b1110, 0b0011)
    WRO = (0b1110, 0b0100)
    WR1 = (0b1110, 0b0101)
    WR2 = (0b1110, 0b0110)
    WR3 = (0b1110, 0b0111)
    SBM = (0b1110, 0b1000)
    RDM = (0b1110, 0b1001)
    RDR = (0b1110, 0b1010)
    ADM = (0b1110, 0b1011)
    RD0 = (0b1110, 0b1100)
    RD1 = (0b1110, 0b1101)
    RD2 = (0b1110, 0b1110)
    RD3 = (0b1110, 0b1111)


def parse_assembly_file(filename):
    return

def fetch():
    return 

def decode(string):
    return

def execute(opcode, operands):
    return

def loop():
    for i in range(100):
        print("4004 is running")
    return

if __name__ == "__main__":
    loop()


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