#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

names = []


invited_names = open("C:/Users/Adrian/PycharmProjects/day-24/Mail Merge Project Start/Input/Names/invited_names.txt", "r")
for name in invited_names:
    name = name.strip("\n")
    names.append(name)
invited_names.close()


starting_letter = open("C:/Users/Adrian/PycharmProjects/day-24/Mail Merge Project Start/Input/Letters/starting_letter.txt")

letter = starting_letter.read()

#print(letter)

for name in names:
    new_letter = letter.replace("[name]", name)
    print(new_letter)
    with open(f"C:/Users/Adrian/PycharmProjects/day-24/Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.docx", mode="w") as completed_letter:
        completed_letter.write(new_letter)

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp