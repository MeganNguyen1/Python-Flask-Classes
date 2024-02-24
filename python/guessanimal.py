# design a "Guess the Animal" game. In this game, the computer "thinks" of one animal from a list and the player has to guess which animal it is by 
# typing its name. There will be only three animals to choose from to keep it extremely simple.
import random

print("Welcome to the Animal Guessing Game")

animals = ["cow", "chicken", "snake", "lion", "cat", "dolphin","pig", "whale", "goat", "penguin"]

animal = random.choice(animals)

print(animal)

guess = input("enter the animal: ")

if guess == animal:
    print("you got it right")
else:
    print("that's wrong")