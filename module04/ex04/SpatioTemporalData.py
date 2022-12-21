'''Implement a class called SpatioTemporalData that takes a dataset
(pandas.DataFrame) as argument in its constructor and implements two methods.'''


from FileLoader import FileLoader


class SpatioTemporalData:
    def __init__(self, df) -> None:
        self.df = df

    def when(self, location):
        df = self.df[self.df['City'] == location]
        years = df[['Year']].drop_duplicates(subset=['Year'])
        return list(record['Year'] for _, record in years.iterrows())

    def where(self, date):
        df = self.df[self.df['Year'] == date]
        cities = df[['City']].drop_duplicates(subset=['City'])
        return list(record['City'] for _, record in cities.iterrows())


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    # pprint.pprint(how_many_medals(data, 'Kjetil Andr Aamodt'))
    sp = SpatioTemporalData(data)
    print(sp.where(1896))
    # Output
    # ['Athina']
    print(sp.where(2016))
    # Output
    # ['Rio de Janeiro']
    print(sp.when('Athina'))
    # Output
    # [2004, 1906, 1896]
    print(sp.when('Paris'))
    # Output
    # [1900, 1924]

    print(sp.where(2000))
    # output is: ['Sydney']

    print(sp.where(1980))
    # output is: ['Lake Placid', 'Moskva'] If a single of these locations is returned it's ok.

    print(sp.when('London'))
    # output is: [2012, 1948, 1908]
