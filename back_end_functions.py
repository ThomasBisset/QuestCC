import random


def random_class():
    """Returns a random class from the list"""
    character_class = [
        "fighter",
        "invoker",
        "ranger",
        "naturalist",
        "doctor",
        "spy",
        "magician",
        "wizard",
    ]
    return random.choice(character_class)


def random_age():
    """Generates a random age."""
    age_range = []
    for _i in range(0, 85):
        age_range.append(random.randint(18, 60))
    for _i in range(0, 10):
        age_range.append(random.randint(61, 200))
    for _i in range(0, 5):
        age_range.append(random.randint(201, 300))
    age = random.choice(age_range)
    return age


def random_height():
    """Randomly picks a height in inches, then converts it to feet and inches"""
    inches = random.randrange(0, 12)
    feet = random.choice([3, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7])
    return f"{feet} feet {inches} inches"


def random_appearance():
    """Returns a random attribute from each list. [0] is the body type description,
    [1] is the face description and [2] is the description of the 'vibe'"""
    body = [
        "scales",
        "worn scars",
        "iridescent skin",
        "rack of muscles",
        "towering physicque",
        "speckled complexion",
        "barrel-sized belly",
        "head of tentacles",
        "generous curves",
        "elongated limbs",
        "bumpy exterior",
        "willowy frame",
        "sculpted hair",
        "stout stature",
        "lived-in body",
        "vestigial tail",
        "webbed fins",
        "rough hide",
    ]
    face = [
        "gaunt face",
        "sharp teeth",
        "fulsome cheeks",
        "large, pointy ears",
        "vestigial antennae",
        "knee-length beard",
        "devestating smile",
        "windswept face",
        "manicured fuzz",
        "ridged forehead",
        "triangular head",
        "timeworn face",
        "romantic eyes",
        "severe jawline",
        "skeptical eyes",
        "radient smile",
        "burning eyes",
        "heavy brows",
    ]
    vibe = [
        "long shadow",
        "sleepy mood",
        "sparkling gaze",
        "eternal grimace",
        "bursting energy",
        "an air of mystery",
        "gentle disposition",
        "androgynous vibes",
        "thousand-yard stare",
        "tightly wound energy",
        "brooding presence",
        "friendly demeanor",
        "meandering gaze",
        "graceful posture",
        "captivating grin",
        "raucous laugh",
        "flawless poise",
        "fiery temper",
    ]
    return random.choice(body), random.choice(face), random.choice(vibe)


def random_clothes():
    """Picks a random item of clothing from a list."""
    clothes = [
        "etched leather armour",
        "a billowing jumpsuit",
        "a tightly fitted tunic",
        "religious vestments",
        "nicked chainmail",
        "runes in my hair",
        "a fluttering cape",
        "weathered rags",
        "a layered dress",
        "a warm cloak",
        "an owl pin",
        "a charmed necklace",
        "a ragged headcover",
        "antique eyeglasses",
        "a patterned hijab",
        "a silken eyepatch",
        "fingerless gloves",
        "a quilted jacket",
        "encrusted cuffs",
        "a feathered cap",
        "a boned bodice",
        "a fancy hat",
        "a bronze breastplate",
        "oversized spectacles",
        "a homemade charm",
        "hammered earrings",
        "an ornamental belt",
        "a shining hauberk",
        "an animal brooch",
        "obsidian bracers",
        "a symbol of god",
        "a tarnished ring",
        "a humble tunic",
    ]
    return random.choice(clothes)


def random_movement():
    """ " Randomly selects a type of movement"""
    movement = [
        "No sense of urgency",
        "an effortless glide",
        "frenzied footwork",
        "a confident step",
        "great difficulty",
        "a reliable pace",
        "wide-swinging arms",
        "a spring in my step",
        "a singular purpose",
        "no sense of space",
        "music in my feet",
        "an uneven gait",
        "a joyful whistle",
        "relentless focus",
        "casual swagger",
        "apprehension",
        "a heavy step",
        "fearlessness",
    ]
    return random.choice(movement)


def random_home():
    """Randomly selects a home"""
    home = [
        "a great metropolis",
        "a remote village",
        "a frontier town",
        "a lonely island",
        "a capital city",
        "a seastead",
        "a remote stronghold",
        "a travelling caravan",
        "a hidden warren",
        "a working farm",
        "a roadside inn",
        "a ship at sea",
        "a place I can't name",
        "a subterrainian city",
        "a forgotten nation",
        "a mountain town",
        "a city in the mist",
        "a homestead",
    ]
    return random.choice(home)


def random_fame():
    """Randomly selects what their home is famous for"""
    fame = [
        "their steady pursuit of pleasure",
        "their easygoing temperament",
        "their unhurried sense of time",
        "treating strangers with love",
        "restoring justice to the land",
        "once ruling a vast empire",
        "creating a world wonder",
        "enduring a great tragedy",
        "their neutral rationality",
        "their warm hospitality",
        "a culture of secrecy",
        "non-heiracical relationships",
        "plainly stating their intentions",
        "their sense of duty to each other",
        "resisting a brutal ruling order",
        "creating historic works of art",
        "strict adherence to the law",
        "their commercial success",
        "setting cultural trends",
        "their traditional ways",
        "inventing the future",
        "losing a great war",
    ]
    return random.choice(fame)


def random_ideal():
    """Selects a random ideal"""
    ideal = [
        "order",
        "justice",
        "heroism",
        "compassion",
        "generosity",
        "pleasure",
        "pragmatism",
        "honor",
        "power",
        "salvation",
        "the ends",
    ]
    return random.choice(ideal)


def random_flaw():
    """Selects a random flaw"""
    flaw = [
        "fearful",
        "megalomaniac",
        "idiot",
        "impish",
        "oblivious",
        "thief",
        "hedonist",
        "liar",
        "reckless",
        "wrathful",
        "vain",
    ]
    return random.choice(flaw)


def random_dream():
    """Selects a random dream"""
    dream = [
        "returning to my hometown as a renowned hero",
        "becoming tremendously wealthy",
        "freeing myself from a gang that wants me dead",
        "finding the source of eternal life",
        "getting revenge on someone who wronged me",
        "becoming a leader of my nation",
        "finding a corner of the world to make my own",
        "becoming a notorious gambler",
        "publishing a book that's found in every home",
        "making every stranger smile",
        "sparking an idea that transforms the world",
        "becoming a master artisan",
        "becoming the greatest scholar in my field",
        "dying an honorable death",
        "recovering a stolen artifact for my people",
        "mapping the entire world",
        "stealing from the rich to give to the poor",
        "meeting the grim reaper",
        "having my name spoken by my leader",
        "pulling off the big score",
        "meeting my parents for the first time",
        "travelling to the stars",
        "spreading my ideal across the land",
        "becoming a celebrity",
        "overturning a corrupt government",
        "meeting my god(s)",
        "producing a timeless work of art",
        "killing my past",
    ]
    return random.choice(dream)
