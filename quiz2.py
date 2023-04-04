# Use the provided list_a and list_b as your starting point.
# Then, perform the following steps:
#
# 1. Create a new list called sol (for solution) consisting of a slice
#    from list_a from the second element through to the word 'it'
# 2. Remove the value 'bad' from sol
# 3. Add a value 'including' so that it is the last value in sol
# 4. Add a value 'good' so that it is the third value in sol
# 5. Add all elements from list_b to the end of sol

list_a = ['this', 'list', 'has', 'bad', 'words', 'in', 'it', 'bad', 'naughty', 'impish']
list_b = ['good', 'nice', 'friendly']
sol=list_a[1:7]
print(sol)
sol.pop(-4)
print(sol)
sol.insert(6,'including')
sol.insert(2,"good")
sol.extend(list_b)  #这里用append会有括号
print(sol)

# Use the set f_suburbs as given as your starting point. Then,
# 1. Remove all suburbs that don't start with a F
# 2. Ensure that the suburbs listed below are in your set
#         Fairfield
#         Fairfield East
#         Fairfield Heights
#         Fairfield West
#         Fairlight
#         Fiddletown
#         Five Dock
#         Flemington
#         Forest Glen
#         Forest Lodge
#         Forestville
#         Freemans Reach
#         Frenchs Forest
#         Freshwater

f_suburbs = {"Randwick", "Kensington", "Frenchs Forest", "Flemington"}
f_suburbs.remove('Randwick')
f_suburbs.remove('Kensington')
new_suburbs = {"Fairfield", "Fairfield East", "Fairfield Heights", "Fairfield West", "Fairlight", "Fiddletown", "Five Dock", "Flemington", "Forest Glen", "Forest Lodge", "Forestville", "Freemans Reach", "Frenchs Forest", "Freshwater"}
f_suburbs.update(new_suburbs)
print(f_suburbs)

# Use the dictionary f_suburbs as given as your starting point.
# This dictionary contains Sydney suburb/population pairs,
# with the mapping going from suburb keys to population values.

# Do the following steps:
# 1. Remove all suburbs that don't start with a F
# 2. Ensure that your dictionary contains:
#
#     Fairfield: 18081
#     Fairfield East: 5273
#     Fairfield Heights: 7517
#     Fairfield West: 11575
#     Fairlight: 5840
#     Fiddletown: 233
#     Five Dock: 9356
#     Flemington: None
#     Forest Glen: None
#     Forest Lodge: 4583
#     Forestville: 8329
#     Freemans Reach: 1973
#     Frenchs Forest: 13473
#     Freshwater: 8866

# The None values indicate the Wikipedia did not have population data.
# These should be INCLUDED in your dictionary.


f_suburbs = {"Randwick": 29986, "Kensington": 15004, "Frenchs Forest": 13473, "Flemington": None}
f_suburbs.pop('Randwick')
f_suburbs.pop('Kensington')
f_suburbs_new={"Fairfield": 18081, "Fairfield East": 5273, "Fairfield Heights": 7517,
               "Fairfield West": 11575, "Fairlight": 5840, "Fiddletown": 233,
               "Five Dock": 9356, "Flemington": None, "Forest Glen": None,
               "Forest Lodge": 4583, "Forestville": 8329, "Freemans Reach": 1973,
               "Frenchs Forest": 13473, "Freshwater": 8866}
f_suburbs.update(f_suburbs_new)
print(f_suburbs)

# Define a few lists...
lst_a = ['a']
lst_b = ['b', lst_a]
lst_c = ['b', ['a']]
print(lst_c)


l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(l[1:4])
print(l[-9:-6])
print(len(l))

t =('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
print(t[:5])
print(t[:-5])
print(t[:-6])

t =('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
print(t[-8:10])
print(t[2:10])
print(t[-7:10])



dic = { ('a', 'b'): 1, 'c': 2 }
print(dic)

tup = (1, 2, ['a', 'b'])
print(tup)
dic = {tup: 'value'}
print(dic)


dic = { ('a', 'b'): 1, 'c': 2,}
print(dic)

