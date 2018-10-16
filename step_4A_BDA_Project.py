"""

    @author = Shardul P Dabholkar, Saurabh Parekh

    This is the step where we provide labelled data to the countries.
    Countires are labelled into 4 categories based on International Evaluation
    Group report which are:

    1. Unsatisfied
    2. moderately Satisfied
    3. Satisfied
    4. Highly satisfied.


    Further we use this labels while building Naive Bayes model in the final step.
    Naive Bayes has been build using Weka. Also as a basis for comparison we have
    also build decision Tree classifier using weka.

"""


import pandas as pd
import numpy as np
import math
import csv


class Feature_four:

    def readCsv(self):

        dFrame = pd.read_csv("paid_unpaid_and_sat_unsat.csv")
        dMatrix = dFrame.as_matrix()
        self.clustering(dMatrix)

    def clustering(self,dMatrix):

        classLabelList = []
        countryList = []

        for row in dMatrix:
            if row[3] <= 98.5909:
                countryList.append(row[0])
                classLabelList.append("Unsatisfied")
            elif row[3] > 98.5909 and row[3] <= 392.1765:
                countryList.append(row[0])
                classLabelList.append("moderately Satisfied")
            elif row[3] > 392.1765 and row[3] <= 786.9231:
                countryList.append(row[0])
                classLabelList.append(" Satisfied ")
            else:
                countryList.append(row[0])
                classLabelList.append(" Highly Satisfied")

        cFrame = pd.read_csv("countries.csv")
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

        with open("Class_Label.csv", "w",newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Country Name","IEG Outcome"])
            writer.writerows(zipped)


def main():

    f4Obj = Feature_four()
    f4Obj.readCsv()

if __name__=="__main__":
    main()