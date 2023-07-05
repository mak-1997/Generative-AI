# problem -1
n = 5
for i in range (0,n) :
    for j in range (0,i+1) :
        print(j+1, end=" ")
    print()

# problem - 2
numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers :
    if num % 5 == 0 and num <= 150 : 
        print(num)
    elif num > 500 :
        break

# problem - 3

s1 = "Ault"
s2 = "Kelly"

mid_index = len(s1)//2
s3 = s1[:mid_index] + s2 + s1[mid_index:]
print(s3)

# problem - 4

str1 = "PyNaTive"
lower = ""
upper = ""
for str in str1 : 
    if str.islower() :
        lower += str
    else :
        upper += str
print(lower + upper)

# problem - 5

def addList (l1, l2) : 
    minLen = min(len(l1), len(l2))
    newList = []
    for i in range(minLen) :
        newList.append(l1[i] + l2[i])
    if(len(l1) > minLen) : 
        newList.extend(l1[minLen:])
    elif(len(l2) > minLen) :
        newList.extend(l2[minLen:])
    return newList

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

print(addList(list1,list2))

# problem - 6

def mixList(l1, l2) :
    newList = []
    for s1 in l1 :
        for s2 in l2 :
            newList.append(s1 + s2)
    return newList

print(mixList(list1,list2))

# problem - 7

def iterate_lists(l1, l2):
    max_length = max(len(l1), len(l2))

    for i in range(max_length):
        out = ""
        if i < len(l1):
            out += l1[i]+" "
        else :
            out += "  "
        if i < len(l2):
            out += l2[-(i + 1)]
        print(out)

iterate_lists(list1, list2)

# problem - 8

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

out = {emp : defaults for emp in employees}
print(out)

# problem - 9

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

new_dict = {key : sample_dict[key] for key in keys}
print(new_dict)

# problem - 10

tuple1 = (11, [22, 33], 44, 55)

lst = list(tuple1)
lst[1][0] = 222
tuple1 = tuple(lst)
print(tuple1)