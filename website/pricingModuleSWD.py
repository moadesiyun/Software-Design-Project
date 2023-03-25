class PricingModule:
    
    def __init__(self, userState, numGal):
        currentPrice = 1.50
        self.userState = userState
        self.numGal = numGal

        if (userState == "TX"):
            locationFactor = 0.02

        else:
            locationFactor = 0.04

        if (self.numGal > 1000):
            galReqFactor = 0.02
        else:
            galReqFactor = 0.03

        #Hard code user to be previous client
        rateHistFactor = 0.01

        margin = (locationFactor - rateHistFactor + galReqFactor + 0.10) * currentPrice

        suggestedPPG = margin + currentPrice

        totalAmtDue = suggestedPPG * numGal

    def getSuggestedPPG():
        return suggestedPPG

    def getTotalAmtDue():
        return totalAmtDue