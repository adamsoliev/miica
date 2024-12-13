#! /usr/bin/python3

RAM = bytearray(640)  # data memory | each 4002 RAM chip consists of 4 of 40-byte banks

ROM = bytearray(4096) # program memory | each 4001 ROM chip is 256-byte

PROGRAM_COUNTER = bytearray(12)         # pc
STACK_REGISTERS = [bytearray(12)] * 3   # stack
INDEX_REGISTERS = [bytearray(4)] * 16   # registers
ACCUMULATOR = bytearray(4)              
TEMPORARY_REGISTER = bytearray(4)       # carry?
INSTRUCTION_REGISTER = bytearray(8)     

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

def main():
    loop()

if __name__ == "__main__":
    main()


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