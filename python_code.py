from pandas import read_csv

file_data = read_csv(r"filename.csv", header=0)

#Below functions will describe our data, good to check and do some preprocessing if required.
print(file_data.values)
print(file_data.columns)
print(file_data.head)
print(file_data.info)
print(file_data.describe)

#Below will plot data into figures.
file_data.plot(x="Year", y="TotalAmount")
file_data.plot(kind='bar', x="Year", y="TotalAmount")
file_data.plot(kind='area')
file_data.plot.scatter(x="Year", y="TotalAmount")
plot.show()

#Create DataFrame for futher use
df = pd.DataFrame(file_data)     
print(df.head)
df_x=df.Year
df_y=df.TotalAmount
df_x=df_x.values.reshape(-1,1)
print(df_y.describe())
