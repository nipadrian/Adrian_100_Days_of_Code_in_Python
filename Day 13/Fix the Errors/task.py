try:
    age = int(input("How old are you?"))
except ValueError:
    print("you have typed in an invalid number. Please try again with a numerical number")
if age > 18:
    print(f"You can drive at age {age}.")
