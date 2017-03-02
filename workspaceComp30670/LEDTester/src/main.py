'''
Created on 28 Feb 2017

@author: David Fottrell
'''
from skimage.external.tifffile.tifffile import FileHandle
from IPython.testing.iptestcontroller import argparser
from pylint.extensions.check_elif import ElseifUsedChecker
if __name__ == '__main__':
    main()

def turnOn(x1, y1, x2, y2):
    # Turn on LED
    for i in range (x1, x2):
        for j in range (y1, y2):
            a2d[i][j] = 1
    return
    
def turnOff(x1, y1, x2, y2):
    #  Turn LED OFF
    for i in range (x1, x2):
        for j in range (y1, y2):
            a2d[i][j] = 0
    return
    
def switch(x1, y1, x2, y2):
    # Toggle LED
    for i in range (x1, x2):
        for j in range (y1, y2):
            if ((a2d[i][j]) == 1):
                a2d[i][j] = 0
            if ((a2d[i][j]) == 0):
                a2d[i][j] = 1                
    return
    
def validCom(str):
    # See also Group Extraction https://developers.google.com/edu/python/regular-expressions
    # Any coordinates outside the range are reset to the extreme values of the array
    import re
    for i in range (0, len(str)):
        match = re.search('(\d*)(\,)(\d*)(\sthrough\s)(\d*)(\,)(\d*)', str)
        x1 = match.group(1)
        if (x1 < 0):
             x1 = 0
        if (x1 > 999):
             x1 = 999
            
        x2 = match.group(3)
        if (x2 < 0):
            x2 = 0
        if (x2 > 999):
             x2 = 999
        
        y1 = match.group(5)
        if (y1 < 0):
            y1 = 0
        if (y1 > 999):
            y1 = 999
            
        y2 = match.group(7)
        if (y1 < 0):
            y1 = 0
        if (y1 > 999):
            y1 = 999

        if (str[:6] == "turn on"):            
            # Need to feed these coordinates to the on() function
            turnOn(x1, x2, y1, y2)
            
        if (str[:7] == "turn off"):
            # LEDState = 0
            # Need to feed these coordinates to the on() function
            turnOff(x1, x2, y1, y2)
            
            # Need to feed these coordinates to the off() function
        if (str[0:6] == "switch"):
            switch(x1, x2, y1, y2)
            # Need to feed these coordinates to the off() function
        
    # Also test the validity of the array being requested, i.e. that you only activate stuff in the array area
    # Test to ensure the command coordinates are consistent, that x1 < x2 and y1 < y2, etc. Otherwise ignore bad coords
    # returns true and the extracted command
    # else returns false
    return

def result():
    # Print reuslt to sceen in the format of [name of input file] [count of lights on]
    pass

def command():
    # Is this necessary, look at valComm...looks like it does everything at the moment!
    
    # After the validCom function has completed, this function takes over to execute the command
    # This should test if there is a switch
    # if there is no switch, it should immediately execute the command
    # If there is a switch, it should call the switch() function
    # It will take in a command, with valid coordinates and LED state and call the appropriate function
    # e.g. It will call turnOn() function and pass the argument for the coordinates
    # That function will return to command
    # Command() will return to calling function
    pass

def main():
    
    import argparse
    import urllib.request
    import pprint
    
    # Initialise an array for the LED
    N = 1000
    a2d = [ [0]*N for_in range(N) ]    
    # pprint(a2d)
    
    # Obtain user input
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help = 'input help')
    args = parser.parse_args()
    filename = args.input
    
    # Validate URL path
    urltest = urllib.request.urlopen(filename)
    if (urltest != 200)
        print("Error - URL is invalid")
    
    # Read the file contents in
    buffer = open(filename).readlines()
    # returns a list, each element of which a  line of the file associated with the file handle
    # Ref John Dunnion's notes from comp10280, lecture 18, slide 15
    # Don't forget to close the file at the end of this script!!
    # buffer.close()
    
    # Line 0 in the test files refers to the size of the array, this next line is a variable to detect that
    asize = int(buffer[0])
    
    # Parse the line in and detect the command to be executed    
    # start at buffer[1] until the end of the file
    for i in range (1, asize):
        if ((validCom(buffer[i])) = true)
            # At this point, pass the returned command to the command function and have it switch on the LED's
            # command()
            # i++
        else
            # i++
            # cycle to the next line
            # not sure if this statement is even necessary
        
     # Count and print the sum of LED's = 1 (on). 0 is off and hence will not affect the sum
     Print(filename, "; The count of LED's on is: ", sum(a2d))
     
        
        
    
    return
