'''
Created on 15 Mar 2017

@author: David Fottrell
'''
import unittest
import time
import datetime
import requests
import os.path

class Test(unittest.TestCase):


    def testValidAPI(self):
        # This is a variable to contain the www.openweathermap.org call for current weather in Dublin with an API key
        srcdata = requests.get('http://api.openweathermap.org/data/2.5/weather?id=7778677&APPID=0b1d40f0f5b1bc4af97416f01400dd72&units=metric')
        self.assertTrue(srcdata.status_code == 200)
        
    
    def testCreateFile(self):
        # This test creates a file with a time stamp and then test it exists afterward
        filestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        # Now concatenate the time stamp with .JSON extention to create a valid filename
        filestamp = filestamp + ".JSON"
        # Now write this file to disk
        filehandle = open(filestamp, 'w')
        filehandle.write("Hello")
        filehandle.close()
        self.assertTrue(os.path.isfile(filestamp))
        
        
    def test_Timer(self):
        counter = 0
        
        while (counter < 12):          # This is for testing phase only, can be deleted in production
            time.sleep(1)               # Timing function waits 1 second
            counter += 1    
        self.assertTrue(counter == 12)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testValidAPI']
    unittest.main()