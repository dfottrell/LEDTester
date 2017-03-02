'''
Created on 28 Feb 2017

@author: David Fottrell
'''
import sys
from nose.tools import *
from src.main import validCom
from src.main import turnOn
from src.main import turnOff
from src.main import switch

N = 10
a2d = [ [0] * N for _ in range(N) ]    
    
def test_validCom():
    eq_(validCom('turn on 0,0 through 9,9'), 'turnOn(0, 0, 9, 9)', 'validCom "turnOn" call failed')
    eq_(validCom('turn off 0,0 through 9,9'), 'turnOff(0, 0, 9, 9)', 'validCom "turnOff" call failed')
    eq_(validCom('switch 0,0 through 9,9'), 'turnOn(0, 0, 9, 9)', 'validCom "switch" call failed')
    
def test_turnOn():
    eq_(turnOn(0, 0, 1, 1), (sum(a2d) == 2), 'turnOn count failed')
    
def test_turnOff():
    eq_(turnOff(0, 0, 1, 1), (sum(a2d) == 0), 'turnOff count failed')
    
def test_switch():
    eq_(switch(0, 0, 1, 1), (sum(a2d) == 2), 'switch count failed')
