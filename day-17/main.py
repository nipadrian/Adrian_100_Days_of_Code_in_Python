

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0


    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Adrian")
user_2 = User("002","Angela")
print(user_1.id)

user_1.follow(user2)



# user_2 = User("002")
#
#
# user_1.id = "001"
# user_1.username = "Adrian"
# user_2 = User()
#
# user_2.id = "002"
# user_2.username = "Jack"

