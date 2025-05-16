yea, idk  
this is kinda a project of me wanting to know what i can do/if i can do this  
dont ask, run main, edit code string in coding file  
its 16-bit  
# CPU.py  
this is the file that emulates the CPU (suprise suprise)  
im gonna make it a wee bit more realistic sometime...  
# GPU.py  
really badly emulates a GPU and screen  
this is big need upgrade  
VRAM is seperate from RAM  
VRAM is technically 256*256 (64 KiB). however, the screen is only 68 px wide and 17 px tall. (1 px is one character)  
# RAM.py
this holds ram class  
this one should be ok  
# allVars.py  
holds any vars that are accessed in multiple files  
mostly.  
# assemb.py  
this one takes Burbx16 assembly - its custom!  
yea  
# coding.py  
this is where fancy magic and anger happen  
this lets you write in BurbLang instead of Burbx16  
thingys that work (\n means new line)  
also " " is ***VERY IMPORTANT*** " ". It is necesary. like so necesary the nonexsistant error detection will get mad  
- for loops:
    - for i 0 <10 +=1\nyour code here\nfrd
- while loops:
  - while i<5\ncode\nwh
- initialize variables:
  - var variable=some value
    - only ints right now and lists (only ints inside) are sorta a thing
- set variables to a value
  - variable=some value
    - this does work with ints, and lists with non variable indexs, only var for list
  - specials (only use like this, not "var")
    - displayMode="auto" - this is base set, updates screen when you draw to it; "manual" - only updates when "disp()" used, this mode uses a lot less processing power; drawing to the screen makes lag, so this is exsist
- add/sub values
   - var+=value or var-=value
   - only ints / int variables
- functions (yay)
   - def function(arg1,arg2,argN)\ncode\nfcd
   - function(parameter1,parameter2,parameterN)
 - special functions:
    -  disp() - when display mode set to manual, this makes screen update
