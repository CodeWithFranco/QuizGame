# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines() # Turn it into a list
#     print(data)

import csv
weather_list = []
with open("weather_data.csv") as weather_data:
    data = csv.reader(weather_data) # creates an object --> at a memory location
    temperature = []
    for row in data:  # Separated each value to row
        if row[1] != "temp":  # Not Equal to temp
            temperature.append(int(row[1]))
    print(temperature)


   