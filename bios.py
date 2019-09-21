#!/usr/bin/python3
import os
import sys
from pathlib import Path

def print_help():
    print("Invalid usage! Usage: bios.py <InFile> <OutFile>")

if len(sys.argv) < 3:
    print_help()

inFile=sys.argv[1]
outFile=sys.argv[2]


byteArray=Path(inFile).read_bytes()

# All blade BIOS's use var 0x3EC == 0x00 as a guard to hide options. Therefore, we can flip the byte to 0x01 to unlock options
# Full String to replace: 0A 82 12 06 EC 03 00 00
#           Suppress If-->|---|
#                      Equals-->|---|
#                      Variable ID-->|---|
#                                  Value-->|---|
#
# In short. Take every occurance of '0A 82 12 06 EC 03 00 00' and replace with '0A 82 12 06 EC 03 00 01'
#                 As decimal:       '10 130 18 6 236 3 0 0'                    '10 130 18 6 236 3 0 1' 
byteArrayNew=[]
unlockCount=0
i = 0
while i < len(byteArray):
    if byteArray[i] == 10 and byteArray[i+1] == 130 and byteArray[i+2] == 18 and byteArray[i+3] == 6 and byteArray[i+4] == 236 and byteArray[i+5] == 3 and byteArray[i+6] == 0 and byteArray[i+7] == 0:
        print("Found suppress if!. Address: {0}".format(hex(i)))
        unlockCount += 1
        byteArrayNew += [10, 130, 18, 6, 236, 3, 0, 1]
        i += 8
    else:
        byteArrayNew.append(byteArray[i])
        i += 1


# Safe guard against writing some really bad data!
if(len(byteArrayNew) != len(byteArray)):
    raise Exception("Source and Dest array do not match! Fatal error!!!!")

open(outFile, "wb").write(bytearray(byteArrayNew))
print("Modified IFR is written to {0}. Options unlocked: {1}!".format(outFile, unlockCount))