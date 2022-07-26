from functions import *

# create chatbot 
home_bot = create_bot('Jordan')

# train all data
train_all_data(home_bot)

# check identity
identity = input("State your identity please: ")

# rules for responding to different identities
# write your code here
if identity=="Mark":
    print("Welcome, Mark. Happy to have you at home.")
elif identity=="Jane":
    print("Mark is out right now, but you are welcome to the house.")
else:
    print("Your access is denied here. ")

# custom data
house_owner = [
    "Who is owner of this house?",
    "Mark Nicholas is the owner of this house."
]
born = [
    "Where was I born?","You were born in Texas."
]
book=[
    "What is my favorite book?",
    "That is easy. Your favourite book is Da Vinci Code"
]
movie=[
    "What is my favorite movie?",
    "You have watched Crazy Rich Asians more times than I can count."
]
sport=[
    "What is my favorite sport?","You have always loved football."
]



custom_train(home_bot, house_owner)
custom_train(home_bot, born)
custom_train(home_bot, book)
custom_train(home_bot, movie)
custom_train(home_bot, sport)

print("------ Training custom data ------")
# write and train your custom data here IF the identity is Mark
# write your code here

# start chatbot
start_chatbot(home_bot)