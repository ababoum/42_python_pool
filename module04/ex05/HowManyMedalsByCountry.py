'''A function that returns a dictionary of dictionaries giving the number and
type of medal for each competition where the country delegation
earned medals'''


import json
from FileLoader import FileLoader

team_sports = ['Basketball', 'Football', 'Tug-Of-War', 'Badminton', 'Sailing',
               'Handball', 'Water Polo', 'Hockey', 'Rowing', 'Bobsleigh', 'Softball',
               'Volleyball', 'Synchronized Swimming', 'Baseball', 'Rugby Sevens',
               'Rugby', 'Lacrosse', 'Polo']

def how_many_medals_by_country(df, country_name):
    res = dict()
    # filter by country
    df = df[df['Team'] == country_name]
    # filter on team_sports only
    df = df[df['Sport'].isin(team_sports)]
    # keep only one record per sport/year
    df = df.drop_duplicates(subset=['Year', 'Sport'], keep='first')
    # sort by year
    df = df.sort_values(by=['Year'])
    for year in df['Year']:
        res[year] = {'G': 0, 'S': 0, 'B': 0}
    for _, row in df.iterrows():
        if row['Medal'] in ['Gold', 'Silver', 'Bronze']:
            res[row['Year']][row['Medal'][0]] += 1
    return res


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    print(how_many_medals_by_country(data, 'United States'))
    print(how_many_medals_by_country(data, "United States") == {1896: {'G': 11, 'S': 7, 'B': 2}, 1900: {'G': 18, 'S': 14, 'B': 13}, 1904: {'G': 65, 'S': 68, 'B': 66}, 1906: {'G': 12, 'S': 6, 'B': 6}, 1908: {'G': 34, 'S': 16, 'B': 15}, 1912: {'G': 46, 'S': 25, 'B': 36}, 1920: {'G': 87, 'S': 41, 'B': 35}, 1924: {'G': 65, 'S': 41, 'B': 36}, 1928: {'G': 39, 'S': 22, 'B': 18}, 1932: {'G': 60, 'S': 57, 'B': 43}, 1936: {'G': 30, 'S': 29, 'B': 28}, 1948: {'G': 57, 'S': 34, 'B': 30}, 1952: {'G': 55, 'S': 38, 'B': 25}, 1956: {'G': 39, 'S': 57, 'B': 21}, 1960: {'G': 83, 'S': 27, 'B': 19}, 1964: {'G': 75, 'S': 36, 'B': 28}, 1968: {
          'G': 86, 'S': 36, 'B': 35}, 1972: {'G': 70, 'S': 58, 'B': 33}, 1976: {'G': 62, 'S': 46, 'B': 30}, 1980: {'G': 24, 'S': 4, 'B': 2}, 1984: {'G': 143, 'S': 75, 'B': 33}, 1988: {'G': 66, 'S': 48, 'B': 36}, 1992: {'G': 79, 'S': 46, 'B': 52}, 1994: {'G': 6, 'S': 8, 'B': 5}, 1996: {'G': 98, 'S': 41, 'B': 28}, 1998: {'G': 25, 'S': 2, 'B': 3}, 2000: {'G': 69, 'S': 34, 'B': 48}, 2002: {'G': 9, 'S': 52, 'B': 9}, 2004: {'G': 65, 'S': 66, 'B': 38}, 2006: {'G': 9, 'S': 7, 'B': 32}, 2008: {'G': 64, 'S': 61, 'B': 47}, 2010: {'G': 8, 'S': 61, 'B': 20}, 2012: {'G': 82, 'S': 44, 'B': 38}, 2014: {'G': 8, 'S': 28, 'B': 16}, 2016: {'G': 95, 'S': 52, 'B': 45}})
