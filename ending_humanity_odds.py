import pandas as pd
from pandas import DataFrame


# -----------------------------------------------------------------------------
# Dictionaries and Lists
# -----------------------------------------------------------------------------
COLNAMES = {"Pursue Advancement_No. The risk is not worth it.":"No",
           "Pursue Advancement_Yes. This is worth pursuing.": "Yes"}

STATENUMLIST = [1.0, 2.0, 4.0,5.0,6.0,8.0,9.0,10.0,11.0, 12.0,13.0,15.0,16.0,17.0,18.0,
             19.0,20.0,21.0,22.0,23.0,24.0,25.0,26.0,27.0,28.0,29.0,30.0,31.0,32.0,33.0,34.0,35.0,36.0,37.0,
             38.0,39.0,40.0,41.0,42.0,44.0,45.0,46.0,47.0,48.0,49.0,50.0,51.0,53.0,54.0,55.0,56.0]

STATETOREGION = {
                 'Alabama': "East South Central",
                 'Alaska': "Pacific",
                 'Arizona': "Mountain",
                 'Arkansas': "West South Central",
                 'California': "Pacific",
                 'Colorado': "Mountain",
                 'Connecticut': "New England",
                 'Delaware': "Middle Atlantic",
                 'District of Columbia': "Middle Atlantic",
                 'Florida': "South Atlantic",
                 'Georgia': "South Atlantic",
                 'Hawaii': "Pacific",
                 'Idaho': "Pacific",
                 'Illinois': "East North Central",
                 'Indiana': "East North Central",
                 'Iowa': "West North Central",
                 'Kansas': "West North Central",
                 'Kentucky':"East South Central",
                 'Louisiana': "West South Central",
                 'Maine': "New England",
                 'Maryland': "Middle Atlantic",
                 'Massachusetts': "New England",
                 'Michigan': "East North Central",
                 'Minnesota': "West North Central",
                 'Mississippi':"East South Central",
                 'Missouri': "West North Central",
                 'Montana': "Mountain",
                 'Nebraska': "West North Central",
                 'Nevada': "Mountain",
                 'New Hampshire': "New England",
                 'New Jersey': "Middle Atlantic",
                 'New Mexico': "Mountain",
                 'New York': "Middle Atlantic",
                 'North Carolina': "South Atlantic", 
                 'North Dakota': "West North Central",
                 'Ohio': "East North Central",
                 'Oklahoma': "West South Central",
                 'Oregon': "Pacific",
                 'Pennsylvania': "Middle Atlantic",
                 'Rhode Island': "New England",
                 'South Carolina': "South Atlantic",
                 'South Dakota': "West North Central",
                 'Tennessee':"East South Central",
                 'Texas': "West South Central",
                 'Utah': "Mountain",
                 'Vermont': "New England",
                 'Virginia': "South Atlantic",
                 'Washington': "Pacific",
                 'West Virginia': "South Atlantic",
                 'Wisconsin': "East North Central",
                 'Wyoming': "Mountain"}

STATE_DICT = {
    1.0: "Alabama",
    2.0: "Alaska",
    4.0: "Arizona",
    5.0: "Arkansas",
    6.0: "California",
    8.0: "Colorado",
    9.0: "Connecticut",
    10.0: "Delaware",
    11.0: "District of Columbia",
    12.0: "Florida",
    13.0: "Georgia",
    15.0: "Hawaii",
    16.0: "Idaho",
    17.0: "Illinois",
    18.0: "Indiana",
    19.0: "Iowa",
    20.0: "Kansas",
    21.0: "Kentucky",
    22.0: "Louisiana",
    23.0: "Maine",
    24.0: "Maryland",
    25.0: "Massachusetts",
    26.0: "Michigan",
    27.0: "Minnesota",
    28.0: "Mississippi",
    29.0: "Missouri",
    30.0: "Montana",
    31.0: "Nebraska",
    32.0: "Nevada",
    33.0: "New Hampshire",
    34.0: "New Jersey",
    35.0: "New Mexico",
    36.0: "New York",
    37.0: "North Carolina",
    38.0: "North Dakota",
    39.0: "Ohio",
    40.0: "Oklahoma",
    41.0: "Oregon",
    42.0: "Pennsylvania",
    44.0: "Rhode Island",
    45.0: "South Carolina",
    46.0: "South Dakota",
    47.0: "Tennessee",
    48.0: "Texas",
    49.0: "Utah",
    50.0: "Vermont",
    51.0: "Virginia",
    53.0: "Washington",
    54.0: "West Virginia",
    55.0: "Wisconsin",
    56.0: "Wyoming"
}
# -----------------------------------------------------------------------------
# Region Data set up
# -----------------------------------------------------------------------------
def byRegions(oddsDf):
    pursuebase = oddsDf[['Pursue Advancement']].copy()
    regionsbase = oddsDf[['US Region']].copy()
    pursueDf = pd.get_dummies(pursuebase)
    pursueDf["US Region"] = regionsbase
    pursueDf = pursueDf.rename(columns = COLNAMES)
    pursueDf= pursueDf.groupby("US Region").sum()
    pursueDf = pursueDf.div(pursueDf.sum(axis=1), axis=0)
    pursueDf["Percentage That Said No"] = pursueDf['No'].apply(lambda x: x*100).round(2)

    statesDf = DataFrame(STATENUMLIST,columns=['id'])
    statesDf['State'] = statesDf['id'].map(STATE_DICT)
    statesDf['US Region'] = statesDf['State'].map(STATETOREGION)

    mergedDf = statesDf.merge(pursueDf, left_on='US Region', right_on='US Region', how = 'left')
    return mergedDf

# -----------------------------------------------------------------------------
# User Decision Comparison
# -----------------------------------------------------------------------------
def ageGenderOdds(oddsDf, odds):
    regionsbase = oddsDf[['US Region']].copy()
    agesdf = oddsDf[['Age Range']].copy()
    gaB = oddsDf[['Gender at Birth']].copy()
    pursuebase=oddsDf[['Pursue Advancement']].copy()
    regionsbase = oddsDf[['US Region']].copy()
    pursueDf = pd.get_dummies(pursuebase)
    pursueDf["US Region"] = regionsbase
    pursueDf["Age Range"] = agesdf
    pursueDf["Gender at Birth"] = gaB
    pursueDf = pursueDf.rename(columns = COLNAMES)
    pursueDf = pursueDf.groupby(["Age Range", "Gender at Birth"]).sum()
    pursueDf['Odds'] = pursueDf['No'] + pursueDf['Yes']
    pursueDf['No'] = pursueDf['No'].div(pursueDf['Odds'])
    pursueDf['Yes'] = pursueDf['Yes'].div(pursueDf['Odds'])
    pursueDf['Odds'] = odds
    return pursueDf

def mergeAgeGenderOdds(df2, df3, df4, df5, df10):
    ago2 = ageGenderOdds(df2, 2)
    ago3 = ageGenderOdds(df3, 3)
    ago4 = ageGenderOdds(df4, 4)
    ago5 = ageGenderOdds(df5, 5)
    ago10 = ageGenderOdds(df10, 10)

    merged = pd.concat([ago2, ago3, ago4, ago5, ago10])
    return merged


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

def main():
    df2 = pd.read_excel("fp--05839-abby-jeff-kyle-will/data/1-in-2-Ending-Humanity.xlsx")
    df3 = pd.read_excel("fp--05839-abby-jeff-kyle-will/data/1-in-3-Ending-Humanity.xlsx")
    df4 = pd.read_excel("fp--05839-abby-jeff-kyle-will/data/1-in-4-Ending-Humanity.xlsx")
    df5 = pd.read_excel("fp--05839-abby-jeff-kyle-will/data/1-in-5-Ending-Humanity.xlsx")
    df10 = pd.read_excel("fp--05839-abby-jeff-kyle-will/data/1-in-10-Ending-Humanity.xlsx")

    groupedDf = mergeAgeGenderOdds(df2,df3,df4,df5,df10)
    groupedDf.to_csv("fp--05839-abby-jeff-kyle-will/data/grouped-Ending-Humanity.csv")

    regions2 = byRegions(df2)
    regions3 = byRegions(df3)
    regions4 = byRegions(df4)
    regions5 = byRegions(df5)
    regions10 = byRegions(df10)

    regions2.to_csv("fp--05839-abby-jeff-kyle-will/data/regions2-Ending-Humanity.csv")
    regions3.to_csv("fp--05839-abby-jeff-kyle-will/data/regions3-Ending-Humanity.csv")
    regions4.to_csv("fp--05839-abby-jeff-kyle-will/data/regions4-Ending-Humanity.csv")
    regions5.to_csv("fp--05839-abby-jeff-kyle-will/data/regions5-Ending-Humanity.csv")
    regions10.to_csv("fp--05839-abby-jeff-kyle-will/data/regions10-Ending-Humanity.csv")

    
# -----------------------------------------------------------------------------
# Script Entry Point
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main()