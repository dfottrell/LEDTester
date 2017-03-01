'''
Created on 28 Feb 2017

@author: David Fottrell
'''
from skimage.external.tifffile.tifffile import FileHandle
from IPython.testing.iptestcontroller import argparser
if __name__ == '__main__':
    main()

def turnOn():
    # Turn on LED
    pass
    
def turnOff():
    #  Turn LED OFF
    pass
    
def switch():
    # Toggle LED
    # This is activated by the command() function when it detects a switch
    # it should determine the LED state at the coordinates given
    # It should then invert the LED state at that location
    # It should recompile the new instruction and pass it back to command() function to execute
    pass
    
def validCom():
    # Extracts the command using regular expression
    # Test if the command is valid, for example if anything beyond turn on, off or switch
    # Also test the validity of the array being requested, i.e. that you only activate stuff in the array area
    # Test to ensure the command coordinates are consistent, that x1 < x2 and y1 < y2, etc. Otherwise ignore bad coords
    # returns true and the extracted command
    # else returns false
    pass

def result():
    # Print reuslt to sceen in the format of [name of input file] [count of lights on]
    pass

def command():
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
    
    # Initialise an array for the LED
    import argparse
    import urllib.request
    import pprint
    
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
    # Ref John Dunnion's notes from comp10280, lecture 18, slide 15
    # Don't forget to close the file at the end of this script!!
    # buffer.close()
    
    # Line 0 in the test files refers to the size of the array, this next line is a variable to detect that
    asize = int(buffer[0])
    
    # Parse the line in and detect the command to be executed    
    # start at buffer[1] until the end of the file
    for i in range (1, asize):
        if (validCom(buffer[i]) = true)
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
