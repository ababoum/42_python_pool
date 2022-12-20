'''Displaying the proportion of participants who played a given sport,
among the participants of a given genders'''

import pandas as pd
from FileLoader import FileLoader

def proportion_by_sport(df, olympic_year, sport, gender):
	df = df[df['Year'] == olympic_year]
	df = df[df['Sex'] == gender]

	df = df.drop_duplicates(subset=['ID', 'Sport'])
	df_sport = df[df['Sport'] == sport]
	return f'{100 * df_sport.shape[0] / df.shape[0]:.2f}%'


if __name__ == "__main__":
	loader = FileLoader()
	data = loader.load('../data/athlete_events.csv')
	print(proportion_by_sport(data, 2004, 'Tennis', 'F'), end = "\n\n")
	# 1.93% or 2.31%
	print(proportion_by_sport(data, 2008, 'Hockey', 'F'), end = "\n\n")
	print(proportion_by_sport(data, 1964, 'Biathlon', 'M'), end = "\n\n")