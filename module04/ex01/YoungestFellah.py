from FileLoader import FileLoader 
import pandas as pd


def youngest_fellah(ds, olympic_year: int):
	if not isinstance(ds, pd.DataFrame) or not isinstance(olympic_year, int):
		return None

	res = dict()
	ds = ds[ds['Year'] == olympic_year]
	res['f'] = ds[ds['Sex'] == 'F']['Age'].min()
	res['m'] = ds[ds['Sex'] == 'M']['Age'].min()
	return res
	

if __name__ == "__main__":
	loader = FileLoader()
	data = loader.load('../data/athlete_events.csv')
	print(youngest_fellah(data, 1992))
	print(youngest_fellah(data, 2004))
	print(youngest_fellah(data, 2010))
	print(youngest_fellah(data, 2003))