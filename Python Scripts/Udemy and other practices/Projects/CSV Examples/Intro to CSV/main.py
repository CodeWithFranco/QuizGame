# # with open("weather_data.csv") as weather_data:
# #     data = weather_data.readlines() # Turn it into a list
# #     print(data)

# import csv
# weather_list = []
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data) # creates an object 
#     temperature = []
#     for row in data:  # Separated each value to row
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")  
print(data["temp"])  # Same as the previous code but easier