from pandas import read_csv

file_data = read_csv(r"filename.csv", header=0)
print(file_data.values)
print(file_data.columns)
print(file_data.head)
print(file_data.info)
print(file_data.describe)
