import unittest
from pricingModuleSWD import *

#Gwyn can work on this file

class testPricingModule(unittest.TestCase):
    def test_location_factor_TX(self):
        testUser = PricingModule("TX", 1000)
        #Expected location factor is 0.02
        self.assertEqual(testUser.getLocationFactor(), 0.02, "Incorrect Location Factor Set for Texas" )
    
    def test_location_factor_Other(self):
        testUser = PricingModule("NY", 1000)
        #Expected location factor is 0.02
        self.assertEqual(testUser.getLocationFactor(), 0.04, "Incorrect Location Factor Set for 'Other'")

    def test_gal_factor_G1000(self):
        testUser = PricingModule("TX", 1001)
        #Expected gal factor is 0.02
        self.assertEqual(testUser.getGalReqFactor(), 0.02, "Incorrect galReqFactor Set for a request greater than 1000")

    def test_gal_factor_L1000(self):
        testUser = PricingModule("TX", 1000)
        #Expected gal factor is 0.03
        self.assertEqual(testUser.getGalReqFactor(),0.03, "Incorrect galReqFactor set for a request less than & equal to 1000")


unittest.main()