states = {42: "Washington", 50: "Hawai", 1: "Delaware"}

print(states[42])
print(states[50])
print(states[1])

states[30] = "Wisconsin"
states[21] = "Illinois"
lenOfSta = len(states)

print(states, lenOfSta)

moreStates = {10: "Virginia", 15: "Kenthucky", 48: "New Mexico"}
print(moreStates)
moreStates[49] = "Arizona"
print(moreStates[49])

evenMoreStates = {3: "New Jersey", 17: "Ohio", 19:"Indiana"}

del evenMoreStates[17]

print(evenMoreStates)
evenMoreStates[17] = "Ohio"