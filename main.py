import random


def random_class():
    class_list = ['fighter', 'invoker', 'ranger', 'naturalist', 'doctor', 'spy', 'magician', 'wizard']
    return random.choice(class_list)


name = input("What is your name?:   ")
pronouns = input("What is your pronouns?:   ")

print("Hello,")
print(f"My name is {name} ({pronouns}).")
print(f"I am {random.randrange(2, 300, 1)} years old and stand {random.randrange(3, 8, 1)} feet tall.")
print(f"I'm the party's {random_class()}.")

