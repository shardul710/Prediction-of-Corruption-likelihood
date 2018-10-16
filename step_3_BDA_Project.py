"""

    @author = Shardul P Dabholkar, Saurabh Parekh

    This step involves selecting the third feature which is Past payment record.
    Some of the things required for this step are performed using Weka.
    Principal Component Analysis has been performed using Weka. K-Means clustering
    has been performed to classify the unlabelled data.

    Eventually after performing PCA and Kmeans Clustering we have have classified the countries
    into 4 Groups based on their past payment record :

    1. Bad
    2. Average
    3. Good
    4. Excellent
"""


import pandas as pd
import numpy as np
import math
import csv


class Feature_three:

    def readCsv(self):

        """

        This method is used to read the data from csv file.

        """

        dFrame = pd.read_csv("paid_unpaid_and_sat_unsat.csv")
        dMatrix = dFrame.as_matrix()
        self.grouping(dMatrix)

    def grouping(self,dMatrix):

        """

        This method is used to group the data together based on centroids obtained using
        K means clustering.

        """

        classLabelList = []
        countryList = []

        for row in dMatrix:
            if row[1] <= 12.1818:
                countryList.append(row[0])
                classLabelList.append("Bad")
            elif row[1] > 12.1818 and row[1] <= 56.7231:
                countryList.append(row[0])
                classLabelList.append("Average")
            elif row[1] > 56.7231 and row[1] <= 367.7059:
                countryList.append(row[0])
                classLabelList.append("Good")
            else :
                countryList.append(row[0])
                classLabelList.append("Excellent")


        cFrame =  pd.read_csv("countries.csv")
        cMatrix = cFrame.as_matrix()

        coList = []
        for row in cMatrix:
            for item2 in countryList:
                if row[0].lower() == item2.lower():
                    coList.append(row[0])

        finalPsList = []
        for i in range(len(coList)):
            for j in range(len(countryList)):
                if coList[i].lower() == countryList[j].lower():
                    finalPsList.append(classLabelList[j])


        zipped = zip(coList,finalPsList)

        with open("feature_Three.csv", "w",newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Country Name","Past Payment Record"])
            writer.writerows(zipped)

def main():
    f3Obj = Feature_three()
    f3Obj.readCsv()

if __name__ == "__main__":
    main()