import unittest 

class PricingModule:
    
    def __init__(self, userState, numGal, rateHist):
        self.currentPrice = 1.50
        self.userState = userState
        self.numGal = numGal
        self.locationFactor = 0
        self.galReqFactor = 0
        self.rateHistFactor = rateHist

        if (userState == "TX"):
            self.locationFactor = 0.02

        else:
            self.locationFactor = 0.04

        if (numGal > 1000):
            self.galReqFactor = 0.02
        else:
            self.galReqFactor = 0.03

        self.margin = (self.locationFactor - self.rateHistFactor + self.galReqFactor + 0.10) * self.currentPrice

        self.suggestedPPG = self.margin + self.currentPrice

        self.totalAmtDue = round(self.suggestedPPG * numGal,2)
        

    def getSuggestedPPG(self):
        return self.suggestedPPG

    def getTotalAmtDue(self):
        return self.totalAmtDue

    def getLocationFactor(self):
        return self.locationFactor
    
    def getGalReqFactor(self):
        return self.galReqFactor


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


if __name__ == '__main__':
    unittest.main()
