import pandas as pd
filePath = '../Public/TestData/test.csv'
dataFrame = pd.read_csv(filePath, sep='\t', dtype=str)
for idx, data in dataFrame.iterrows():
	print(data)