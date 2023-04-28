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