# with open("weather_data.csv") as weather_data:
#     weather = weather_data.readlines()
#
# print(weather)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             row[1] = int(row[1])
#             temperatures.append(row[1])
#
#     print(temperatures)

    # for row in range(1,len(data)):
    #     temperatures.append(row[1])

import pandas

data = pandas.read_csv("weather_data.csv")
#print(data)
#print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# n = (len(temp_list))
#
# sum = sum(temp_list)
# average = sum/n
#
# print(average)
# print(data["temp"].mean())
#
# print(data["temp"].max())
#
#
# # get data in columns
# print(data["condition"]) # like a key
# print(data.condition) # like an object
#
# # get data in row
# print(data[data.day == "Monday"])
#print(data[data["day"]])
# max_temperature = data["temp"].max()
# print(max_temperature)
# # row data of weather data that temperature was max
# print(data[data.temp == data["temp"].max()])
#
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday)
print(monday.temp[0])
monday_temp = monday.temp[0]

monday_temp_f = monday_temp * 9/5+32
print(monday_temp_f)


# create dataframe from scratch
# data_dict = {
# #     "students": ["Amy", "James", "Angela"],
# #     "scores": [76, 56, 65]
# # }
# #
# # data = pandas.DataFrame(data_dict)
# # data.to_csv("new_data.csv")


# data = pandas.read_csv("squirrel_count.csv")
# print(data["Primary Fur Color"])
#
# gray_count = (len(data[data["Primary Fur Color"] == "Gray"]))
# red_count = (len(data[data["Primary Fur Color"] == "Cinnamon"]))
# black_count = (len(data[data["Primary Fur Color"] == "Black"]))
#
# #create dataframe from scratch
# data_dict = {
#     "Fur Color": ["gray", "red", "black"],
#     "Count": [gray_count, red_count, black_count]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("Fur_color_count.csv")