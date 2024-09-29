# TODO-1: Ask the user for input
import art
print(art.logo)


def find_highest_bidder(bidders):
    highest_bid = 0
    highest_bidder = ""

    for people in bidders:
        bid_amount = bidders[people]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            highest_bidder = people
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")





bidders = {}

other_bidders = True

while other_bidders == True:
    name = input("What is your name?")
    bid = input("What is your bid?")

    bidders[name] = int(bid)

    #response = ""

    other_bidders = input("are there any other bidders? Type 'yes' or 'no'").lower()
    if other_bidders == "yes":
        print("\n"*20)
        other_bidders = True
    elif other_bidders == "no":
        other_bidders = False
    else:
            print("please type 'yes' or 'no'")

    #while response != "yes" or response != "no":
    #    response = input("are there any other bidders? Type 'yes' or 'no'").lower()
    #    if response == "yes":
    #        other_bidders = True
    #    elif response == "no":
    #        other_bidders = False
    #    else:
    #        print("please type 'yes' or 'no'")

#max_bidder = max(bidders, key=bidders.get)
#max_bid = max(bidders.values())

find_highest_bidder(bidders)

#print(max_bidder)
#print(max_bid)

#print(bidders)
#print(f"The winner is {max_bidder} with a bid of ${max_bid}.")

# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


def find_highest_bidder(bidders):
    highest_bid = 0
    highest_bidder = ""

    for people in bidders:
        bid_amount = bidders[people]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            highest_bidder = people
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")


