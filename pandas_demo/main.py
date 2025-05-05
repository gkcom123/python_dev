import csv
import pandas
# with open('weather_data.csv') as csv_data:
#     content = csv_data.readlines()
#     print(content)
#
# with open('weather_data.csv') as csv_data_file:
#     rows = csv.reader(csv_data_file)
#     temperatures = []
#     for row in rows:
#         print(row[1])
#         if(row[1] != 'temp'):
#             temperatures.append(int(row[1]))
#
#     print(temperatures)
# data = pandas.read_csv('weather_data.csv')
# print(data['temp'])
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data['temp'].to_list()
# print(temp_list)
# print(data['temp'].max())
# print(data[data['day'] == 'Monday'])
# print(data[data['temp'].max() == data['temp']])
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pandas.DataFrame(data)
# print(df)
# df.to_csv('output.csv', index=False)  # Save data to CSV
# for (key,value) in df.items():
#     print(value)

for (index, row) in df.iterrows():
    print(row)