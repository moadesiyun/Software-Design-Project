import unittest

from requestForm import *
from dbmodels import *

class testRequestForm(unittest.TestCase):
    def test_gal_req_None(self):
        testuser = requestForm(None)
        self.expectedFailure('Must specify number of gallons')

    def test_gal_req_not_int(self):
        testuser = requestForm(1.2)
        self.expectedFailure('Gallons requested must be a number greater than zero')

unittest.main()

#Loryn can work on this file

#Helpful link to learn/understand unit tests <3
#https://machinelearningmastery.com/a-gentle-introduction-to-unit-testing-in-python/

#Create class for each test to be completed
#Basically see if the program, when broken, deals with the invalid input properly (eg. flash error, set to 0, etc.)
#In our case, we most likely want to make sure the invalid input isn't saved in the profile/calculation/etc.