import unittest
from pricingModuleSWD import *

#Gwyn can work on this file

class testPricingModule(unittest.TestCase):
    def test_location_factor_TX(self):
        testUser = PricingModule("TX", 1000, 0.1)
        #Expected location factor is 0.02
        self.assertEqual(testUser.getLocationFactor(), 0.02, "Incorrect Location Factor Set for Texas" )
    
    def test_location_factor_Other(self):
        testUser = PricingModule("NY", 1000, 0.1)
        #Expected location factor is 0.02
        self.assertEqual(testUser.getLocationFactor(), 0.04, "Incorrect Location Factor Set for 'Other'")

    def test_gal_factor_G1000(self):
        testUser = PricingModule("TX", 1001, 0.1)
        #Expected gal factor is 0.02
        self.assertEqual(testUser.getGalReqFactor(), 0.02, "Incorrect galReqFactor Set for a request greater than 1000")

    def test_gal_factor_L1000(self):
        testUser = PricingModule("TX", 1000, 0.1)
        #Expected gal factor is 0.03
        self.assertEqual(testUser.getGalReqFactor(),0.03, "Incorrect galReqFactor set for a request less than & equal to 1000")

    def test_suggested_PPG(self):
        testUser1 = PricingModule("TX", 1000, 0.01)
        #location factor = 0.02, galReqFactor =  0.03
        #Expected PPG = 1.71
        self.assertEqual(testUser1.getSuggestedPPG(), 1.71, "Incorrect PPG for testUser1")
    
    def test_total_amt_due(self):
        testUser = PricingModule("TX", 5000, 0)
        #location factor = 0.02, galRegFactor = 0.02
        #Expected total amount due = 8,550
        self.assertEqual(testUser.getTotalAmtDue(), 8550, "Incorect Total for test user")

unittest.main()
