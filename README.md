# EDL to CDL
![image](https://github.com/user-attachments/assets/2fae7206-1f47-4c0b-89cd-7b248cd3f81d)

This is the source code repository. 
Please look under the [releases](https://github.com/emilemassie/edl_to_cdl/releases) for the pre-compiled, executable versions of the program. 

## Features.
                                 
This tool reads a CMX3600-like Edit Decision List (EDL) file, extracts all the Color Decision Lists (CDLs) contained within, and exports them in various formats:

- .cdl: A single Color Decision List file.
- .cc: A single color correction file.
- .ccc: A collection of color corrections.

CDLs are named or assigned IDs based on the EDL tapenames. For footage from ARRI, RED, or similar cameras, with tapenames like "A001[_]C009[...]", the utility recognizes and uses "A001C001" as the tapename in IDs within the CCC file or as filenames for individual CDLs/CCs within a folder.

## Original Code:
This utility is based on a script by Walter Arrighetti, PhD, originally written in 2017.

## Source Code
The source code is public and has been tested on Python 3.11. This version is a modified adaptation of Walter Arrighetti's code, updated for Python 3 compatibility, with an added GUI for ease of use.
