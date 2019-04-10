from pandas import read_csv

boston = read_csv(r"filename.csv", header=0)
print(boston.values)
print(boston.columns)
print(boston.head)
print(boston.info)
print(boston.describe)
