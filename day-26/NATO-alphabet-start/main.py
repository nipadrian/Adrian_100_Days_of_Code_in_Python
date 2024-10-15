student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    # print(key)
    # print(value)
    pass

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    # print(index)
    # print(row.student)
    # print(row.score)
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

df = pd.read_csv("nato_phonetic_alphabet.csv")
#print(df)

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

nato_dict = {row.letter:row.code for (index,row) in df.iterrows()}
print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Give me a word and I will phoneticize it!")

letter_list = [letter.upper() for letter in word]
# new_list = []
#
# print(letter_list)
# #print(nato_dict["A"])
# for letter in letter_list:
#     if letter in nato_dict:
#         new_list.append(nato_dict[letter])
# print(new_list)

new_list1 = []

new_list1 = [nato_dict[letter] for letter in letter_list if letter in nato_dict]

print(new_list1)