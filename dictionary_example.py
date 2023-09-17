captains = {}
captains['Enterprise'] = 'Picard'
captains['Voyager'] = 'Janeway'
captains['Defiant'] = 'Sisko'
if 'Enterprise' in captains :
    print("Key Enterprise exists in the dictionary")
else :
    captains['Enterprise'] = 'Unknown'
if 'Discovery' in captains :
    print("Key Discovery exists in the dictionary")
else :
    captains['Discovery'] = 'Unknown'
    print(f"The ship Discovery is {captains['Discovery']}")
for ship in captains:
    print(f"The {ship} is captained by {captains[ship]}")
del captains['Discovery']