
import pandas as pd


def load(path: str) -> pd.DataFrame:
	'''takes in a string (csv file) and outputs the data as a pandas dataframe
	'''
	try:
		assert isinstance(path, str), "the file name has to be a string"
		dataframe = pd.read_csv(path, index_col=0)
		print("Loading dataset of dimensions " + str(dataframe.shape))
		return dataframe
	except AssertionError as msg:
		print("AssertionError: " + str(msg))
	except FileNotFoundError:
		print("Error: file not found")
