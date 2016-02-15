# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 15:32:50 2016

@author: miffyvo
"""

# Codes for boxplot "Amount.Requested'
import matplotlib.pyplot as plt
import pandas as pd

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)
import matplotlib.pyplot as plt
import pandas as pd

loansData.boxplot(column='Amount.Requested')
plt.savefig("boxplot1.png")

#codes for histogram "Amount.Requested"
loansData.hist(column='Amount.Funded.By.Investors')
plt.savefig("hist1.png")

#codes for qq plot "Amount.Requested"
import scipy.stats as stats

plt.figure()
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.savefig("probplot1.png")

