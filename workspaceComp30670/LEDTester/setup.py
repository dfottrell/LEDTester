'''
Created on 28 Feb 2017

@author: David Fottrell
'''

from setuptools import setup
from setuptools.dist import check_entry_points

setup(name="LEDTester",
      version="0.1",
      description="LED Tester for COMP30670 Assignment 3",
      url="",
      author="David Fottrell",
      author_email="david.fottrell@ucdconnect.ie",
      licence="GPL3",
      packages=["src"],
      entry_points={
          'console_scripts':['workspaceComp30670_LEDTester=src.main:main']
          }
    
    )