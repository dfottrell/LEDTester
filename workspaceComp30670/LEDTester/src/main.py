'''
Created on 28 Feb 2017

@author: David Fottrell
'''

def main():


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
        
    def validCom(s):
        # See also Group Extraction https://developers.google.com/edu/python/regular-expressions
        # Any coordinates outside the range are reset to the extreme values of the array
        import re
        for i in range (0, len(s)):
            match = re.search('(\d*)(\,)(\d*)(\sthrough\s)(\d*)(\,)(\d*)', s)
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
    
            if (s[:6] == "turn on"):            
                # Need to feed these coordinates to the on() function
                turnOn(x1, x2, y1, y2)
                
            if (s[:7] == "turn off"):
                # LEDState = 0
                # Need to feed these coordinates to the on() function
                turnOff(x1, x2, y1, y2)
                
                # Need to feed these coordinates to the off() function
            if (s[0:6] == "switch"):
                switch(x1, x2, y1, y2)
                # Need to feed these coordinates to the off() function
            
        return
    

    
    import argparse
    import urllib.request
    
    # Initialise an array for the LED
    N = 1000
    a2d = [ [0] * N for _ in range(N) ]    
    # pprint(a2d)
    
    # Obtain user input
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help = 'input help')
    args = parser.parse_args()
    filename = args.input
    
    # Validate URL path
    urltest = urllib.request.urlopen(filename)
    if (urltest != 200):
        print("Error - URL is invalid")
    
    # Read the file contents in
    buffer = open(filename).readline()
    # Line 0 in the test files refers to the size of the array, this next line is a variable to detect that
    # asize = int(buffer[0]) don't seem to need this after all!
    for line in buffer:
        for i in range(len(buffer)):
            validCom(buffer[i])
    
    # Close file for neatness sake
    buffer.close()
    print(filename, "; Count of LEDs on are ", sum(a2d))
    
    return

if __name__ == '__main__':
    main()
