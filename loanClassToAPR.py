# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 09:42:53 2021
@author: Richard Paglia

"""

class loan(object):
    def __init__(self, name):
        self._name = name

    def who(self):
        print(self._name)

    def setPV(self, PV):
        self._PV = PV
        print('present value = ', self._PV)

    def setRate(self, ratePct):
        #set interest, apr
        self._ratePct = ratePct
        print('APR = ', self._ratePct,'%')

    def setMonths(self, months):
        self._months = months
        print(self._months, 'months')

    def computePmt(self):
        r = self._ratePct/100/12
        self._Pmt = self._PV*(r*(1+r)**self._months)/((1+r)**self._months-1)
        print('payment = $', round(self._Pmt,2))
        return self._Pmt
    
    def setPmt(self, Pmt):
        self._Pmt = Pmt
        print('Max/month = $', self._Pmt)
              
    def computePV(self):
        r = self._ratePct/100/12
        n = self._months
        self._PV = (self._Pmt*(1-(1+r)**(-n)))/r
        print('You can borrow $', round(self._PV,2))
        return self._PV

    def computeAPR(self):
        n = self._months
        PV = self._PV
        Pmt = self._Pmt
        epsilon = .00001
        rT = 100
        rB = 1*(10**-27)
        rTry=(rT + rB)/2
        while(abs((PV-(Pmt*(1-(1+rTry)**(-n)))/rTry))>=epsilon):
            rTry = (rT + rB)/2
            if(PV-(Pmt*(1-(1+rTry)**(-n)))/rTry)>epsilon:
                rT=rTry
            if(PV-(Pmt*(1-(1+rTry)**(-n)))/rTry)<epsilon:
                rB=rTry
        self._ratePct = rTry*100*12
        print("APR = ",self._ratePct, "%")
        return self._ratePct

if __name__ == "__main__":
    loan1 = loan('Richie')
    loan1.who()

    loan1.setPV(1)
    loan1.setMonths(12)
    loan1.setPmt(.1)
    APR=loan1.computeAPR()
    loan1.setRate(APR)
    loan1.computePV()
    loan1.computePmt()