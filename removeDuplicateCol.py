__author__ = 'wzhang'

import itertools
from collections import Counter

def removeDuplicateCol(df):

    """

    :param df: pandas DataFrame
    :return: pandas DataFrame with unique column names
    """

    dfCol = list(df.columns)

    dfColDict = Counter(dfCol)
    duplicates = [i[0] for i in dfColDict.items() if i[1] > 1]

    if duplicates <> []:

        dfCol2 = dfCol
        duplicatesIndex = {}
        for i in duplicates:
            ocurrences = []
            start = 0
            while dfCol2.count(i) > 0:
                start += dfCol2.index(i)
                ocurrences.append(start)
                cutoff = dfCol2.index(i)+1
                dfCol2 = dfCol2[cutoff:]
                start += 1
            duplicatesIndex[i] = ocurrences
            dfCol2 = dfCol

        duplicatesIndexList = [duplicatesIndex[i][1:] for i in duplicatesIndex]
        duplicatesIndexList = list(itertools.chain(*duplicatesIndexList))
        restCols = list(set(range(len(dfCol))) - set(duplicatesIndexList))

        for col in restCols:
            dfCol[col] = "duplicates"
        df.columns = dfCol
        dfNew = df.drop("duplicates")

    else:

        dfNew = df

    return dfNew



