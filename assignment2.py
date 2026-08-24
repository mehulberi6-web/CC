#ASSIGNMENT 2 - Q1
roll = 1024160063

L = []

for i in str(roll):
    L.append(int(i) * 10)

print("L =", L)

L.append(50)
print("After append:", L)

L.insert(2, 70)
print("After insert:", L)

L.remove(50)
print("After remove:", L)

L.pop()
print("After pop:", L)

L.sort()
print("Ascending:", L)

L.sort(reverse=True)
print("Descending:", L)

print("First three:", L[:3])
print("Last three:", L[-3:])

avg = sum(L) / len(L)

new_list = [x for x in L if x > avg]

print("Elements greater than average:", new_list)


#Assignment 2- Q2
l=[70, 60, 40, 30, 20, 10, 10, 0]
scores = tuple(L[:8])

print("Scores:", scores)

highest = max(scores)
print("Highest score:", highest)
print("Index:", scores.index(highest))

lowest = min(scores)
print("Lowest score:", lowest)
print("Count:", scores.count(lowest))

rev = list(scores[::-1])
print("Reversed list:", rev)



x = int(input("Enter a score: "))

if x in scores:
    print("First occurrence index:", scores.index(x))
else:
    print("Score not present")

try:
    scores[0] = 100
except TypeError as e:
    print("Error:", e)

first, second, *remaining = scores
print(first)
print(second)
print(remaining)


#Assignment 2 - Q3
import random

roll = 1024160063

random.seed(roll)

numbers = []

for i in range(100):
    numbers.append(random.randint(100, 900))

print("Numbers:", numbers)

odd = 0
even = 0

for x in numbers:
    if x % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Odd numbers:", odd)
print("Even numbers:", even)

def prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

prime_numbers = [x for x in numbers if prime(x)]

print("Prime numbers:", prime_numbers)
print("Number of prime numbers:", len(prime_numbers))

most = max(set(numbers), key=numbers.count)

print("Most frequent number:", most)
print("Frequency:", numbers.count(most))



#Assignment 2 - Q4
L = [1,0,2,4,1,6,0,0,6,3]
A = {digit*7 for digit in L}
B = {digit*9 for digit in L}
print("Set A: ", A)
print("Set B: ", B)

print("Union =", A.union(B))
print("Intersection =", A.intersection(B))

print("A - B =", A.difference(B))
print("B - A =", B.difference(A))


print("Symmetric difference =", A.symmetric_difference(B))

print("A subset of B:", A.issubset(B))
print("B superset of A:", B.issuperset(A))

x = int(input("Enter a value to remove from A: "))

A.discard(x)



print("A after removing:", A)


#Assignment 2 - Q5
my_dict = {
    "name": "Mehul",
    "roll_no": "1024160063",
    "branch": "C0SE",
    "age": 20,
    "city": "ferozepur"
}

city = my_dict.pop("city")
my_dict["location"] = city

my_dict["cgpa"] = 8.0

my_dict["age"] = my_dict["age"] + 1

dict1 = my_dict.copy()
dict1.pop("branch")

dict2 = my_dict.copy()
del dict2["branch"]

print("Using pop:", dict1)
print("Using del:", dict2)

for key, value in my_dict.items():
    print(key, "->", value)

if "email" in my_dict:
    print(my_dict["email"])
else:
    print("Email not present")

friend_dict = {
    "name": "Ansh",
    "roll_no": "1024160039",
    "branch": "C0SE",
    "age": 20,
    "city": "Amritsar"
}

merged = {**my_dict, **friend_dict}

print("Merged dictionary:", merged)

string_dict = {key: value for key, value in my_dict.items() if isinstance(value, str)}

print("String values:", string_dict)
