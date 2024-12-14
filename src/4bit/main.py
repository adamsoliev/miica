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
from typing import List, Union

class OP(Enum):
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
    FIM = 0b0010_0000  # Fetch immediate data to register pair
    FIN = 0b0011_0000  # Fetch indirect from ROM

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
    JIN = 0b0011_0001  # Jump indirect
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
    SRC = 0b0010_0001
    WRM = 0b1110_0000
    WMP = 0b1110_0001
    WRR = 0b1110_0010
    WPM = 0b1110_0011
    WRO = 0b1110_0100
    WR1 = 0b1110_0101
    WR2 = 0b1110_0110
    WR3 = 0b1110_0111
    SBM = 0b1110_1000
    RDM = 0b1110_1001
    RDR = 0b1110_1010
    ADM = 0b1110_1011
    RD0 = 0b1110_1100
    RD1 = 0b1110_1101
    RD2 = 0b1110_1110
    RD3 = 0b1110_1111

parsed = [32, 32, 13, 11, 33, 224, 15, 7, 6, 7, 32, 32, 13, 11, 33, 228, 15, 229, 15, 230, 15, 231, 15, 6, 7, 4, 0, 0, 0, 0, 0, 0]

def parse_assembly_file(filename: str) -> List[tuple[OP, int]]:
    instructions: List[tuple[OP, int]] = []
    with open(filename, 'r') as file:
        for line in file:
            if ':' not in line or not line.strip():
                continue
            bytes_str: List[str] = line.split(':')[1].strip().split()
            i: int = 0
            while i < len(bytes_str):
                instruction: tuple[OP, int] = (OP.NOP, -1)

                first_opr: int = int(bytes_str[i][0], 16)
                first_opa: int = int(bytes_str[i][1], 16)
                if first_opr == 0x1:
                    second_opr: int = int(bytes_str[i + 1][0], 16)
                    second_opa: int = int(bytes_str[i + 1][1], 16)
                    d = (first_opa << 8) | (second_opr << 4) | second_opa

                    instruction = (OP.JCN, d)
                    i += 2
                elif first_opr in {0x2, 0x3}:
                    if first_opr == 0x2:
                        if first_opa & 0b1 == 0:
                            second_opr: int = int(bytes_str[i + 1][0], 16)
                            second_opa: int = int(bytes_str[i + 1][1], 16)
                            d = (first_opa << 8) | (second_opr << 4) | second_opa
                            instruction = (OP.FIM, d)
                            i += 2
                        else:
                            instruction = (OP.SRC, second_opa)
                            i += 1
                    else:
                        instruction = (OP.FIN if (first_opa & 0b1) == 0 else OP.JIN, second_opa)
                        i += 1
                elif first_opr in {0x4,0x5,0x7}:
                    second_opr: int = int(bytes_str[i + 1][0], 16)
                    second_opa: int = int(bytes_str[i + 1][1], 16)
                    d = (first_opa << 8) | (second_opr << 4) | second_opa

                    instruction = (OP.JUN if first_opr == 0x4 else OP.JMS if first_opr == 0x5 else OP.ISZ, d)
                    i += 2
                elif first_opr == 0xE:
                    instruction = (OP((first_opr << 4) | first_opa), 0) # no 2nd part in tuple since 1st has it already
                    i += 1
                else:
                    instruction = (OP(first_opr), second_opa)
                    i += 1

                # assert instruction[1] != -1
                instructions.append(instruction)

    instruction_values: List[int] = [int(instr[0].value) for instr in instructions]
    assert instruction_values == parsed
    return instructions


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