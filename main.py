import game_data
import art
import random

def compare_followers(user_guess, first_count, second_count):
    if first_count > second_count:
        return user_guess == "A"
    else:
        return user_guess == "B"

def get_new_item():
    return random.choice(game_data.data)

item1 = get_new_item()
item2 = get_new_item()

if item1 == item2:
    item2 = get_new_item()

score = 0
game_over = False

print(art.logo)

while not game_over:
    item1 = item2
    item2 = get_new_item()
    
    print(f"Compare A: {item1['name']}, a {item1['description']}, from {item1['country']}.")
    print(art.vs)
    print(f"Against B: {item2['name']}, a {item2['description']}, from {item2['country']}.")
    
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    
    if compare_followers(user_choice, item1["follower_count"], item2["follower_count"]):
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_over = True
