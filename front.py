from back import (
    random_age,
    random_appearance,
    random_class,
    random_clothes,
    random_dream,
    random_fame,
    random_flaw,
    random_height,
    random_home,
    random_ideal,
    random_movement,
)


# Take user input for name and pronouns TODO: Random options?
name = input("What is your name?:       ")
pronouns = input("What is your pronouns?:   ")

# For testing purposes, uncomment if needed
# name = "Test"
# pronouns = "test/test"

# Print character sheet to screen
print("Hello,")
print(f"My name is {name} ({pronouns}).")
print(f"I am {random_age()} years old and stand {random_height()} feet tall.")
print(f"I'm the party's {random_class()}.")
print(f"When people first see me, they notice my {random_appearance()[0]}; ", end="")
print(f"{random_appearance()[1]}; and {random_appearance()[2]}.")
print(f"I wear {random_clothes()}; {random_clothes()}; and move with {random_movement()}.")
print(f"I'm from {random_home()} where my people are known for {random_fame()}.")
print(f"I believe in {random_ideal()}, but my {random_flaw()} side can get in my way.")
print(f"I dream of {random_dream()}.")
