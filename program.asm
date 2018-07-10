movi R0, 0x0;
movi R1, 0x4;
addi R0, R0, 0x1;
and R2, R0, R1;
jz R2, 0x2;
movi R3, 0x1;
nop ;
jumpi 0;