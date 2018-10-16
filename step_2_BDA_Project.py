"""

    @author = Shardul P Dabholkar, Saurabh Parekh

    This step involved extracting the feature of Income group that was given.
    Income group plays an important role in our model, since income group is directly
    proportional to the tax collected by the government. If government has large amount
    of taxes collected it shows that it can repay the funds it has taken from world bank.

"""

import pandas as pd
import numpy as np
import math
import csv

class Feature_Two:

    def readCsv(self):

        """

        This method is used to read the data from csv and map it to the countries
        we have considered for our model.

        """
        cFrame =  pd.read_csv("countries.csv")
        cMatrix = cFrame.as_matrix()

        dFrame = pd.read_csv("feature_two.csv")
        dMatrix = dFrame.as_matrix()

        countriesList = []
        incomeGroupList = []
        for row1 in cMatrix:
            for row2 in dMatrix:
                if row1[0].lower() == row2[0].lower():
                    countriesList.append(row1[0])
                    incomeGroupList.append(row2[1])

        zipped = zip(countriesList,incomeGroupList)

        with open("feature_TwoA.csv", "w",newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Country Name","Income group"])
            writer.writerows(zipped)


def main():
    ftwoObj = Feature_Two()
    ftwoObj.readCsv()

if __name__ == "__main__":
    main()