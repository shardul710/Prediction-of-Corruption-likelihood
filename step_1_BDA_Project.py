"""

    @author = Shardul P Dabholkar, Saurabh Parekh

    This step involes data cleaning and extraction of feature termed as CorruptionIndex.
    CorruptionIndex for previous years has been given. We compute the mean of CorruptionIndex
    of those particular years. Then we have used otsu method to compute the threshold which
    can be used to identify the Countries as per CorruptionIndex in 2 categories:
        1. High
        2. Low

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv


class Corruption:
    """
    
        This class is used to generate feature "CorruptionIndex" required for Fraud Detection.
    
    """

    def __init__(self):

        self.corruptionDict = {}
        self.dataDict = {}

    def findThreshold(self,corrIndexList,countryList):
        """
        This method finds the threshold and classify the countries using that threshold.
        """
        threshold = 9.99537520559  # computed using otsu method
        highCorrList = []
        lowCorrList = []
        ctrList1 = []
        ctrList2 = []

        classList = []

        for i in range(len(corrIndexList)):
            if corrIndexList[i] <= threshold:
                classList.append('high')
            else:
                classList.append('low')

        for i in range(len(corrIndexList)):
            if corrIndexList[i] <= threshold:
                ctrList1.append(i)
                highCorrList.append(corrIndexList[i])
            else:
                ctrList2.append(i)
                lowCorrList.append(corrIndexList[i])

        zipped = zip(countryList,classList)
        with open("feature_OneB.csv", "w",newline='') as f:
            writer = csv.writer(f)
            writer.writerows(zipped)


        plt.scatter(ctrList1,highCorrList,c='red',marker='v')
        plt.scatter(ctrList2,lowCorrList,c='blue',marker='o')
        plt.show()


    def plotCorruptionIndex(self,countryNumberList,corrIndexList,countryList):

        """

        This method is used to plot the Corruption Index of Country using scatter plots.

        """

        plt.scatter(countryNumberList,corrIndexList,c="blue",marker="v")
        plt.xlabel("Countries")
        plt.ylabel("CorruptionIndex")
        plt.show()
        self.findThreshold(corrIndexList,countryList)

    def dataClean(self):

        """

        This method  is used for data cleaning purpose.

        """

        dataFrame = pd.read_csv("CorruptionIndex.csv")
        matrix = dataFrame.as_matrix()

        cFrame = pd.read_csv("feature_One_A.csv")
        cMatrix = cFrame.as_matrix()

        datalist = []
        for row in matrix:
            flag = True
            mlist = []
            for i in range(len(row)):
                if row[i] == '-':
                    flag = False
                    break
                else:
                    for ctry in cMatrix:
                        if row[0].lower() == ctry[0].lower():
                            mlist.append(row[i])

            if flag == True:
                datalist.append(mlist)

        # writing data to the file
        with open("cleanedCorruptionIndexA.csv", "w",newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Jurisdiction","1998","1999","2000","2001","2002","2003","2004","2005",
                             "2006","2007","2008","2009","2010","2011","2012","2013","2014","2015"])
            writer.writerows(datalist)



    def readCsv(self):
        """

        This method is used to read the data from csv into a data frame.

        """
        dataFrame = pd.read_csv("cleanedCorruptionIndexA.csv")
        matrix = dataFrame.as_matrix()
        countryList = []
        corrIndexList = []
        rownum = 0

        for row in matrix:
            sum = 0
            countryList.append(row[0])
            for i in range(1,len(row)):
                sum += float(row[i])

            corrIndexList.append(sum/len(row)-1)

        countryNumberList = []
        for i in range(len(countryList)):
            print(countryList[i]+" : "+str(corrIndexList[i]))
            countryNumberList.append(i+1)


        zipped = zip(countryList, corrIndexList)

        #print(countryList)
        #print(corrIndexList)

        self.plotCorruptionIndex(countryNumberList,corrIndexList,countryList)


def main():
    corrObj = Corruption()
    #corrObj.dataClean()
    corrObj.readCsv()

if __name__=="__main__":
    main()
