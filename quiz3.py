l = ["Fairfield",
    "Fairfield East",
    "Fairfield Heights",
    "Fairfield West",
    "Fairlight",
    "Fiddletown",
    "Five Dock",
    "Flemington",
    "Forest Glen",
    "Forest Lodge",
    "Forestville",
    "Freemans Reach",
    "Frenchs Forest",
    "Freshwater"]
for elem in l:
    if not elem[:6] == "Forest":
        print(elem)


f_suburbs = dict()
f_suburbs["Fairfield"] = 18081
f_suburbs["Fairfield East"] = 5273
f_suburbs["Fairfield Heights"] = 7517
f_suburbs["Fairfield West"] = 11575
f_suburbs["Fairlight"] = 5840
f_suburbs["Fiddletown"] = 233
f_suburbs["Five Dock"] = 9356
f_suburbs["Flemington"] = None
f_suburbs["Forest Glen"] = None
f_suburbs["Forest Lodge"] = 4583
f_suburbs["Forestville"] = 8329
f_suburbs["Freemans Reach"] = 1973
f_suburbs["Frenchs Forest"] = 13473
f_suburbs["Freshwater"] = 8866

for suburb, population in f_suburbs.items():
    if suburb.startswith("F") and not suburb.startswith("Forest") and population is not None:
        print(suburb + ": " + str(population))


first_names = ['Dwayne', 'Ryan', 'Mark', 'Ben', 'Vin']
middle_names = ['"The Rock"', 'Rodney', 'Robert Michael', 'Geza', None]
last_names = ['Johnson', 'Reynolds', 'Wahlberg', 'Affleck', 'Diesel']
for last in last_names:
    for first in first_names:
        for middle in middle_names:
            if middle:
                print(f"{first} {middle} {last}")
            else:
                print(f"{first} {last}")

l = ["Fairfield",
    "Fairfield East",
    "Fairfield Heights",
    "Fairfield West",
    "Fairlight",
    "Fiddletown",
    "Five Dock",
    "Flemington",
    "Forest Glen",
    "Forest Lodge",
    "Forestville",
    "Freemans Reach",
    "Frenchs Forest",
    "Freshwater"]
print(len(l))

for i in range(len(l)):
    print(f"{i}: {l[i]}")

for x in range(1, 101):
    if x % 3 == 0 and x % 5 != 0:
        print(str(x) + ": Fizz")
    elif x % 5 == 0 and x % 3 != 0:
        print(str(x) + ": Buzz")
    elif x % 3 == 0 and x % 5 == 0:
        print(str(x) + ": FIZZ BUZZ")
    else:
        print(str(x))



s={'a','c','d'}
print('a' in s or 'b' not in s)
print('a' in s or not ('b' in s))
print(not('a' not in s and 'b' in s))

def process_string(s):
    words=s.lower()
    words=words.split()
    return words
print(process_string('This is my test String'))

def process_string(s):
    words = s.lower()
    words = s.split()
    return words
print(process_string('This is my test String'))


def process_string(s):
    words=s.split()
    x=[]
    for i,j in enumerate(words):
        if i%2==0:
            x.append(j.lower())
        else:
            x.append(j.upper())

    return x
print(process_string('This is my test String'))




def fizz_buzz_sumz(i):
    j = 0
    sum_all = 0
    while j <= i:
        if j % 3 == 0 and j % 5 != 0:
            sum_all += j*3
        elif j % 5 == 0 and j % 3 != 0:
            sum_all += j*5
        elif j % 3 == 0 and j % 5 == 0:
            sum_all += 0
        else:
            sum_all += j
        j += 1
    print(sum_all)
fizz_buzz_sumz(10)
