from functions import *</br>

# create chatbot
</br>
home_bot = create_bot('Jordan')</br>

# train all data
</br>
train_all_data(home_bot)</br>

# check identity
</br>
identity = input("State your identity please: ")</br>

# rules for responding to different identities
</br>
if identity=="Mark":</br>
    print("Welcome, Mark. Happy to have you at home.")</br>
elif identity=="Jane":</br>
    print("Mark is out right now, but you are welcome to the house.")</br>
else:</br>
    print("Your access is denied here. ")</br>

# custom data 
</br>
house_owner = [</br>
    "Who is owner of this house?",</br>
    "Mark Nicholas is the owner of this house."</br>
]</br>
born = [</br>
    "Where was I born?","You were born in Texas."</br>
]</br>
book=[</br>
    "What is my favorite book?",</br>
    "That is easy. Your favourite book is Da Vinci Code"</br>
]</br>
movie=[</br>
    "What is my favorite movie?",</br>
    "You have watched Crazy Rich Asians more times than I can count."</br>
]</br>
sport=[</br>
    "What is my favorite sport?","You have always loved football."</br>
]</br>



custom_train(home_bot, house_owner)</br>
custom_train(home_bot, born)</br>
custom_train(home_bot, book)</br>
custom_train(home_bot, movie)</br>
custom_train(home_bot, sport)</br>

print("------ Training custom data ------")</br>

# start chatbot
</br>
start_chatbot(home_bot)</br>
