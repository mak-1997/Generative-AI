# Question link ->   https://masai-school.notion.site/S1-D3-Assignment-Set-3-2eeb3485b99e4942b20badbcdf76c9c3

# problem -1

list1 =  [("John", 25), ("Jane", 30)]

for name, age in list1 :
    print(f"{name} is {age} years old")

# problem -2

def add_person(dictionary, name, age):
    dictionary[name] = age

def update_age(dictionary, name, new_age):
    if name in dictionary :
        dictionary[name] = new_age
    else :
        print("this name is not present in the database")

def delete_person(dictionary, name):
    if name in dictionary :
        del dictionary[name]

def perform_operations():
    people = {}

    while True:
        operation = input("Enter operation (add/update/delete), and enter q to exit: ").strip()
        if operation == "q" :
            return
        if operation == "add":
            name = input("Enter name: ").strip()
            age = int(input("Enter age: "))
            add_person(people, name, age)
        elif operation == "update":
            name = input("Enter name: ")
            new_age = int(input("Enter new age: "))
            update_age(people, name, new_age)
        elif operation == "delete":
            name = input("Enter name: ")
            delete_person(people, name)
        else:
            print("Not a valid input.")
            continue
        
        print(people)

perform_operations()

# problem -3

def twoSum (list, target) :
    list.sort()
    l = 0
    r = len(list)-1
    while l < r :
        if list[l] + list[r] < target :
            l += 1
        elif list[l] + list[r] > target :
            r -= 1
        else :
            return [l,r]
    return "Does not exist"

print(twoSum([2, 7, 11, 15],10))

# problem -3

def checkPalindrome (str) : 
    l = 0
    r = len(str)-1
    while l < r :
        if str[l] != str[r] :
            print(f"The word {str} is not a palindrome.")
            return
        else :
            l += 1
            r -= 1
    print(f"The word {str} is a palindrome.")

checkPalindrome("madmm")

# problem -4

def selectionSort (list) :
    for i in range(len(list)-1) :
        for j in range(i+1, len(list)) :
            if list[i] > list[j] :
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    
    return list

list2 = [64, 25, 12, 22, 11]
print(selectionSort(list2))

# problem -5

from queue import LifoQueue

def stack_operations(operations):
    stack = LifoQueue()
    output = []

    for operation in operations:
        if operation.startswith('push'):
            value = operation.split('(')[1].split(')')[0]
            stack.put(value)
        elif operation == 'pop()':
            if not stack.empty():
                output.append(stack.get())
            else:
                output.append(None)

    return output

operations = ['push(1)', 'push(2)', 'pop()', 'push(3)', 'pop()', 'pop()']
result = stack_operations(operations)
print(result)

# problem -6

def fizzBuzz () :
    for i in range(1,101) :
        if i % 3 == 0 and i % 5 == 0 :
            print("FizzBuzz")
        elif i % 5 == 0 :
            print("Buzz")
        elif i % 3 == 0 :
            print("Fizz")
        else :
            print(i)

fizzBuzz()


# problem -7

def count_words(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()
        word_count = len(content.split())

    with open(output_file, 'w') as file:
        file.write(f"Number of words: {word_count}")

input_file = "input.txt"
output_file = "output.txt"
count_words(input_file, output_file)

# problem -8

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."

num1 = 5
num2 = 0
result = divide_numbers(num1, num2)
print(result)
