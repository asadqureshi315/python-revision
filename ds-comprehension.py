users = [
    {"name": "Asad", "age": 25},
    {"name": "Ali", "age": 30},
    {"name": "Sara", "age": 22},
]
# Dictionary comprehension
hsh= {i['name']:i['age'] for i in users}

hsh= {i['name']:i['age'] for i in users if i['age']>=25 }

ifElse={"adult" if age >= 18 else "minor" for age in ages}

scores = {
    "Asad": 80,
    "Ali": 95,
    "Sara": 88
}
for k,v in scores.items():
    print(k,v)
scores= {k:v+5 for k,v in scores.items()}

freq = {"a": 3, "b": 2}
freq["c"] #returns nothing
freq.get("c", 0) # returns fallback value i.e 0 if no c in freq, DOES NOT SET c AS 0 in freq

from collections import defaultdict
pairs = [
    ("fruit", "apple"),
    ("fruit", "banana"),
    ("vegetable", "carrot"),
]
hsh={}
for i in pairs:
    hsh[i[0]]=hsh.get(i[0],[])+[i[1]]

print(hsh)

# Default Dict 
from collections import defaultdict
pairs = [
    ("fruit", "apple"),
    ("fruit", "banana"),
    ("vegetable", "carrot"),
]
hsh = defaultdict(list) # defaultdict() needs a default factory telling it what value to create for a missing key
for category, item in pairs:
    hsh[category].append(item)
print(hsh)

# COUNTER
from collections import Counter
word = "banana"
c=Counter(word)
print(c)
c["a"]        # 3
c["x"]        # 0, not KeyError
c.most_common(1)   # [('a', 3)]


# List comprehension
names= [i['name'] for i in users if i['age']>=25]
age= [i['age'] for i in users if i['age']>=25]

for ind,name in enumerate(names,1):
    print(ind, name)

# Zip returns an iterator
zipped=zip(names,ages)
print(list(zipped))

for name,age in zipped:
    print(name,age)

print(list(zipped))
#unzipping
n,a=zip(*zipped)
print(n,a)

print(next(zipped)) # (Asad,25)
print(next(zipped)) # (Ali,30)
print(list(zipped)) # [(Sara,22)]

# Tupple
point = (10, 20)
x,y=point
print(x,y)

nums = [10, 20, 30, 40, 50]
first,*middle,end=nums
print(first,middle,end)

nums = [1, 2, 3, 4, 5, 6]
first,*rest=nums
print(first,rest)

# Sets
nums = [1, 2, 2, 3, 4, 4, 5]
s=set(nums)
print(s)
print(3 in s) # Takes O(1), set are hash based

seen = set()
result = []

for num in nums:
    if num not in seen:
        seen.add(num)
        result.append(num)

print(result)

# Sorted
users = [
    ("Asad", 25),
    ("Ali", 30),
    ("Sara", 22),
]
sort=sorted(users, key=lambda x:x[1], reverse=True)   # Returns a new list
users.sort(key=lambda x: x[1])   # Mutates original users
sort=sorted(users, key=lambda x:len(x[0]))  # Get longest name first
print(sort)

