'''Fileloader class containing a load and a display method'''

import sys
import pandas as pd

class FileLoader:
	def __init__(self) -> None:
		pass

	def load(self, path):
		try:
			dataset = pd.read_csv(path)
		except:
			print("Error while opening the dataset file")
			return None

		print(f'Loading dataset of dimensions {dataset.shape[0]} x {dataset.shape[1]}')
		return dataset

	def display(self, df, n):
		if not isinstance(df, pd.DataFrame) or not isinstance(n, int):
			return None

		if n > 0:
			print(df.head(n=n))
		elif n < 0:
			print(df.tail(n=-n))


if __name__ == "__main__":
	fl = FileLoader()

	df = fl.load("../data/athlete_events.csv")

	fl.display(df, 5)
	fl.display(df, -5)
