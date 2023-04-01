import random


def random_class():
    character_class = [
        'fighter', 'invoker', 'ranger', 'naturalist', 'doctor', 'spy', 'magician', 'wizard'
    ]
    return random.choice(character_class)


def random_appearance():
    body = [
        'scales', 'worn scars', 'iridescent skin', 'rack of muscles', 'towering physicque',
        'speckled complexion', 'barrel-sized belly', 'head of tentacles', 'generous curves',
        'elongated limbs', 'bumpy exterior', 'willowy frame', 'sculpted hair', 'stout stature',
        'lived-in body', 'vestigial tail', 'webbed fins', 'rough hide'
    ]
    face = [
        'gaunt face', 'sharp teeth', 'fulsome cheeks', 'large, pointy ears', 'vestigial antennae',
        'knee-length beard', 'devestating smile', 'windswept face', 'manicured fuzz', 
        'ridgid forehead', 'triangular head', 'timeworn face', 'romantic eyes', 'severe jawline',
        'skeptical eyes', 'radient smile', 'burning eyes', 'heavy brows'
    ]
    vibe = [
        'long shadow', 'sleepy mood', 'sparkling gaze', 'eternal grimace', 'bursting energy',
        'an air of mystery', 'gentle disposition', 'androgynous vibes', 'thousand-yard stare',
        'tightly wound energy', 'brooding presence', 'friendly demeanor', 'meandering gaze', 
        'graceful posture', 'captivating grin', 'raucous laugh', 'flawless poise', 'fiery temper'
    ]
    return random.choice(body), random.choice(face), random.choice(vibe)


def random_clothes():
    clothes = [
        'etched leather armour', 'a billowing jumpsuit', 'a tightly fitted tunic', 
        'religious vestments', 'nicked chainmail', 'runes in my hair', 'a fluttering cape',
        'weathered rags', 'a layered dress', 'a warm cloak', 'an owl pin', 
        'a charmed necklace', 'a ragged headcover', 'antique eyeglasses', 'a patterned hijab',
        'a silken eyepatch', 'fingerless gloves', 'a quilted jacket', 'encrusted cuffs',
        'a feathered cap', 'a boned bodice', 'a fancy hat', 'a bronze breastplate', 
        'oversized spectacles', 'a homemade charm', 'hammered earrings', 'an ornamental belt',
        'a shining hauberk', 'an animal brooch', 'obsidian bracers', 'a symbol of god',
        'a tarnished ring', 'a humble tunic'
    ]
    return random.choice(clothes)


name = input("What is your name?:   ")
pronouns = input("What is your pronouns?:   ")

print("Hello,")
print(f"My name is {name} ({pronouns}).")
print(f"I am {random.randrange(2, 300, 1)} years old and stand {random.randrange(3, 8, 1)} feet tall.")
print(f"I'm the party's {random_class()}.")
