
#This is a really reallyt rough draft :')
class PricingModule:
    
    def __init__(self, currentPrice, userState, numGal):
        self.currentPrice = currentPrice
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
    rateHistFactor = 0.01

    margin = (locationFactor - rateHistFactor + galReqFactor + 0.10) * currentPrice

    suggestedPPG = margin + currentPrice

    totalAmtDue = suggestedPPG * numGal

    def getSuggestedPPG():
        return suggestedPPG

    def getTotalAmtDue():
        return totalAmtDue