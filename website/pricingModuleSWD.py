class PricingModule:
    
    def __init__(self, userState, numGal, rateHist):
        currentPrice = 1.50
        self.userState = userState
        self.numGal = numGal

        if (userState == "TX"):
            locationFactor = 0.02

        else:
            locationFactor = 0.04

        if (numGal > 1000):
            galReqFactor = 0.02
        else:
            galReqFactor = 0.03

        #Hard code user to be previous client
        rateHistFactor = rateHist

        margin = (locationFactor - rateHistFactor + galReqFactor + 0.10) * currentPrice

        self.suggestedPPG = margin + currentPrice

        self.totalAmtDue = round(self.suggestedPPG * numGal,2)
        

    def getSuggestedPPG(self):
        return self.suggestedPPG

    def getTotalAmtDue(self):
        return self.totalAmtDue