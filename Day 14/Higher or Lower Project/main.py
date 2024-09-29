import random
import game_data
import art

#Import art for higher and lower
print(art.logo)

# Call random key - Compare A: Kylie Jenner, a reality tv personality and businesswomen and
# self made billionare, from united states.

# Length of dictionary = 50
#print(len(game_data.data))

game = True
score = 0

while game is True:


    dict_count = len(game_data.data)


    number = random.randint(0, dict_count-1)
    data_nameA = (game_data.data[number]['name'])
    data_descriptionA = (game_data.data[number]['description'])
    data_locationA = (game_data.data[number]['country'])
    data_followersA = (game_data.data[number]['follower_count'])
    print(f"Compare A: {data_nameA}, a {data_descriptionA}, from {data_locationA}.")
    del game_data.data[number]


    # add VS. art
    print(art.vs)

    # call random key -
    dict_count = len(game_data.data)
    number = random.randint(0, dict_count-1)
    data_nameB = (game_data.data[number]['name'])
    data_descriptionB = (game_data.data[number]['description'])
    data_locationB = (game_data.data[number]['country'])
    data_followersB = (game_data.data[number]['follower_count'])
    print(f"Against B: {data_nameB}, a {data_descriptionB}. from {data_locationB}.")
    del game_data.data[number]

    # Input who has more followers? Type A or B:
    decision = input("Who has more followers? Type 'A' or 'B':").lower()
    print("\n"*20)
    if data_followersA > data_followersB and decision == 'a':
        score += 1
        print(f"You're right! Current Score: {score}")
        game = True
    elif data_followersA < data_followersB and decision == 'a':
        # end game
        print(f"Sorry, that's wrong. Final score: {score}")
        game = False
    elif data_followersB > data_followersA and decision == 'b':
        score += 1
        print(f"You're right! Current Score: {score}")
        game = True
    elif data_followersB < data_followersA and decision == 'b':
        # end game
        print(f"Sorry, that's wrong. Final score: {score}")
        game = False

# If then statement to see who wins

# increment score by 1 if win, exit out and say you lose if wrong


# When you get the answer wrong, output "Sorry, that's wrong. Final score: ___
