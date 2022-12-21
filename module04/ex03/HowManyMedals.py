'''Implement a function that will return a dictionary of dictionaries
giving the number and type of medals for each year during which the participant
won medals.'''

import json
import pprint
import pandas as pd
from FileLoader import FileLoader


def how_many_medals(df, name):
    res = dict()
    df = df[df['Name'] == name]

    years = df[['Year']].drop_duplicates(subset=['Year'])
    for year in years['Year']:
        res[year] = {'G': 0, 'S': 0, 'B': 0}
    for _, row in df.iterrows():
        if row['Medal'] in ['Gold', 'Silver', 'Bronze']:
            res[row['Year']][row['Medal'][0]] += 1
    return res


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    # pprint.pprint(how_many_medals(data, 'Kjetil Andr Aamodt'))
    print(json.dumps(how_many_medals(
        data, 'Kjetil Andr Aamodt'), indent=2, sort_keys=False))
    # Output
    # {1992: {'G': 1, 'S': 0, 'B': 1},
    # 1994: {'G': 0, 'S': 2, 'B': 1},
    # 1998: {'G': 0, 'S': 0, 'B': 0},
    # 2002: {'G': 2, 'S': 0, 'B': 0},
    # 2006: {'G': 1, 'S': 0, 'B': 0}}

    print(how_many_medals(data, 'Gary Abraham'))
    #  the output is: "{1976: {'G': 0, 'S': 0, 'B': 0}, 1980: {'G': 0, 'S': 0, 'B': 1}}"

    print(how_many_medals(data, 'Yekaterina Konstantinovna Abramova'))
    #  the output is "{2006: {'G': 0, 'S': 0, 'B': 1}, 2010: {'G': 0, 'S': 0, 'B': 0}}"

    print(how_many_medals(data, 'Kristin Otto'))
    #  the output is: "{1988: {'G': 6, 'S': 0, 'B': 0}}"
