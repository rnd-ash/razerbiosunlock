# razerbiosunlock

# Setup
1. Download UEFI Tool Version 0.24.0 (newer versions do not allow replacing modules!) [download here](https://github.com/LongSoft/UEFITool/releases/tag/0.24.0)

2. Load up your rom file in UEFITool. Locate the 'setup' module. Usually searching the word 'Overclock' takes you directly to the module
3. Right click the setup module -> Extract body.

4. Run python script on the extracted body

5. When done, right click the module, and click replace body. Replace with the outputFile from the script

6. Save and flash!

# Usage
```
python3 bios.py inputFile outputFile
```


