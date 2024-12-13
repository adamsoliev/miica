
### The Intel 4004, released in 1971, was the first commercially produced processor. 

## Key Features

- **4-bit Processor**: Operates on 4-bit data units (nibbles), making it ideal for binary-coded decimal (BCD) arithmetic.
- **Clock Speed**: Runs at up to 740 kHz, with an instruction cycle of approximately 10.8 microseconds, executing ~92,000 instructions per second.
- **Instruction Set**: A BCD-oriented instruction set with 46 instructions, using an 8-bit instruction format.
- **Addressing**: Utilizes a 12-bit address bus, allowing access to up to 4 KB of ROM and 640 bytes of RAM.
- **Registers**: Includes sixteen 4-bit general-purpose registers grouped into pairs for addressing and operations.
- **Package**: Implemented in a 16-pin DIP package with multiplexed data and address lines to minimize pin count.

## Physical chip
<a href="https://en.wikipedia.org/wiki/Intel_4004" target="_blank">
    <img src="../../assets/4bit/1_1080px-Intel_C4004_b.jpg" alt="The ceramic C4004 variant" width="25%">
</a>

## Architecture
<a href="https://en.wikipedia.org/wiki/Intel_4004" target="_blank">
    <img src="../../assets/4bit/2_952px-4004_arch.png" alt="The ceramic C4004 variant" width="80%">
</a>

- **Harvard Architecture**: Separates program memory (ROM) and data memory (RAM).
- **Memory Access**: Requires multiple clock cycles to fetch instructions or data due to multiplexing.
- **Components**: Part of the MCS-4 family, which includes:
  - The 4004 CPU
  - ROM chips for storing programs
  - RAM chips for data storage
  - Shift-register chips for I/O handling

## DIP chip pinout
<a href="https://en.wikipedia.org/wiki/Intel_4004" target="_blank">
    <img src="../../assets/4bit/3_640px-Intel_4004_processor_pinout.png" alt="The ceramic C4004 variant" width="25%">
</a>

## Resources

- **Datasheet**: [Intel 4004 Datasheet](https://datasheets.chipdb.org/Intel/MCS-4/datashts/intel-4004.pdf)
- **Emulator**: [Intel 4004 Emulator](http://e4004.szyc.org/emu/)
- **Blogs**: [The Strangeness of the Intel 4004](https://thechipletter.substack.com/p/the-strangeness-of-the-intel-4004)