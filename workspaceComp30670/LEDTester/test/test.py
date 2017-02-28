'''
Created on 28 Feb 2017

@author: David Fottrell
'''
import sys
from nose.tools import *

# T1 - Test that the program can open, close and read a line from an external file source
# T2 - Test the first 3 lines read in from the user input file are properly formatted commands 
# T3 - Test if the command is a switch, skip to T5 if false.  May need a regular expression here!
# T4 - If T3 is true, test if you have correctly reformatted the array with the toggled LED? e.g. was on, switch it off 
# T5 - Repeating test 2, count the number of LED's left on and verify the number is correct
# T6 - Repeat test with deliberately corrupted instructions, e.g. white space, negative array coordinates, etc.
