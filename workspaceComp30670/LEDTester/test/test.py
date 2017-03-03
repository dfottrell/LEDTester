'''
Created on 28 Feb 2017

@author: David Fottrell
'''
import sys
from nose.tools import *
from src.main import LEDTest

N = 5
a2d = [ [0] * N for _ in range(N) ]    

s1 = 'turn on 0,0 through 5,5'
s2 = 'turn off 0,0 through 5,5'
s3 = 'switch 0,0 through 5,5'
    
def test_validCom():
    eq_(LEDTest.validCom(a2d, s1), (LEDTest.turnOn(a2d, 0, 0, 5, 5)), "LEDon test failed")
    eq_(LEDTest.validCom(a2d, s2), (LEDTest.turnOff(a2d, 0, 0, 5, 5)), "LEDOff test failed")
    eq_(LEDTest.validCom(a2d, s3), (LEDTest.switch(a2d, 0, 0, 5, 5)), "switch test failed")
    
def test_turnOn():
    eq_(LEDTest.turnOn(0, 0, 1, 1), (sum(a2d) == 2), 'turnOn count failed')
    
def test_turnOff():
    eq_(LEDTest.turnOff(0, 0, 1, 1), (sum(a2d) == 0), 'turnOff count failed')
    
def test_switch():
    eq_(LEDTest.switch(0, 0, 1, 1), (sum(a2d) == 2), 'switch count failed')
