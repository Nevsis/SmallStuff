#!/usr/bin/env python3
import os
import sys
import fileinput
import fnmatch

# takes multiple arguments as long as they are csv files and given relative to the script location
filepaths = [str(arg) for arg in sys.argv[1:]]

for path in filepaths:
    # path relative to the script location
    file = os.path.join(os.path.dirname(__file__), path)
    if not os.path.splitext(path)[1] in {'.csv', '.CSV'}:
        print ("Could not convert %s, because no csv file extension.", path)
        continue
    with fileinput.FileInput(file, inplace = True) as f: 
        for line in f:       
            print(line.replace(';',',', 1), end='')
    
        

    
