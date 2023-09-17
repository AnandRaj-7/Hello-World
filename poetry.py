#####Automatic poem generator####
#### 9.5 Challenge: Wax Poetic ####
import random
def make_poem():
    noun1 = ""
    noun2 = ""
    noun3 = ""
    verb1 = ""
    verb2 = ""
    verb3 = ""
    adjective1 = ""
    adjective2 = ""
    adjective3 = ""
    adverb1 = ""
    preposition1 = ""
    preposition2 = ""
    nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla", "boy"]
    verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
    adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
    prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
    adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]
    while (noun1 == noun2 or noun2 == noun3 or noun1 == noun3):
        noun1 = random.choice(nouns)
        noun2 = random.choice(nouns)
        noun3 = random.choice(nouns)
    while (verb1 == verb2 or verb2 == verb3 or verb1 == verb3):
        verb1 = random.choice(verbs)
        verb2 = random.choice(verbs)
        verb3 = random.choice(verbs)
    while (adjective1 == adjective2 or adjective2 == adjective3 or adjective1 == adjective3):
        adjective1 = random.choice(adjectives)
        adjective2 = random.choice(adjectives)
        adjective3 = random.choice(adjectives)
    adverb1 = random.choice(adverbs)
    while (preposition1 == preposition2):   
        preposition1 = random.choice(prepositions)
        preposition2 = random.choice(prepositions)
    x = "A"
    y = "a"
    if adjective1.startswith("a") or adjective1.startswith("e") or adjective1.startswith("i") or adjective1.startswith("o") or adjective1.startswith("u"):
        x = "An"
    else:
        x = "A"
    if adjective3.startswith("a") or adjective3.startswith("e") or adjective3.startswith("i") or adjective3.startswith("o") or adjective3.startswith("u"):
        y = "an"
    else:
        y = "a"
    poem  = f"\n{x} {adjective1} {noun1}\n\n{x} {adjective1} {noun1} {verb1} {preposition1} the {adjective2} {noun2}\n{adverb1}, the {noun1} {verb2}\nthe {noun2} {verb3} {preposition2} {y} {adjective3} {noun3}\n"
    return poem 
new_poem = make_poem()
print(new_poem)