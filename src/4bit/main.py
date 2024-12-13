#! /usr/bin/python3

RAM = bytearray(640)  # data memory | each 4002 RAM chip is 40-byte

ROM = bytearray(4096) # program memory | each 4001 ROM chip is 256-byte

PROGRAM_COUNTER = bytearray(12)         # pc
STACK_REGISTERS = [bytearray(12)] * 3   # stack
INDEX_REGISTERS = [bytearray(4)] * 16   # registers
ACCUMULATOR = bytearray(4)              
TEMPORARY_REGISTER = bytearray(4)       # carry?
INSTRUCTION_REGISTER = bytearray(8)     

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
