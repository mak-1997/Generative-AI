print("Hello, World!")

# ////////////////////////////////////

integer = 5
print("Type of integer : " + str(type(integer)) + ", value: " + str(integer) )
float = 3.14
print("Type of float : " + str(type(float)) + ", value: " + str(float) )
string = "mayank"
print("Type of string : " + str(type(string)) + ", value: " + str(string) )
boolean = True
print("Type of boolean : " + str(type(boolean)) + ", value: " + str(boolean) )
number_list = [1,2,3,4,5,6,]
print("Type of number_list : " + str(type(number_list)) + ", value: " + str(number_list) )
tuple = ("fw20_0447","mayank", 25)
print("Type of tuple : " + str(type(tuple)) + ", value: " + str(tuple) )
dictionary = {
    "name" : "mayank",
    "age" : 25
}
print("Type of dictionary : " + str(type(dictionary)) + ", value: " + str(dictionary) )
set = {"apple", "banana", "orange", "apple"}
print("Type of set : " + str(type(set)) + ", value: " + str(set) )

# //////////////////////////////////////////////////////////////////////////////////////////////

numbers_list = list(range(1 , 11))
print("original list : " , numbers_list)

# Adding a number in the end of the list
numbers_list.append(-11)
numbers_list.append(-51)
print("appended list : " , numbers_list)

# removing a number from the list
numbers_list.remove(5)
print("removed list : " , numbers_list)

numbers_list.sort()
print("sorted list : " , numbers_list)

# //////////////////////////////////////////////////////////////////////////////////////////////////

# print the sum and average of a list of numbers.

sum_numbers = sum(numbers_list)
average = sum_numbers/len(numbers_list);
print("Sum:" + str(sum_numbers) + ", Average:" + str(average))

# //////////////////////////////////////////////////////////////////////

#  Write a Python function that takes a string and returns the string in reverse order.
def reverse_string (str):
    return str[::-1]

print(reverse_string("Hello World !"))

# //////////////////////////////////////////////////

# Write a Python program that counts the number of vowels in a given string.

def count_vowels (str):
    vowels = "aeiouAEIOU"
    count = 0

    for char in str :
        if char in vowels :
            count += 1

    return count

print(count_vowels("mayank singh"))

# //////////////////////////////////////////////////////////////

#  Write a Python function that checks whether a given number is a prime number.

def is_prime (num) :
    if num < 2 :
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0 :
            return False
    return True

num = 7

if is_prime(num) :
    print(num, "is prime number")
else :
    print(num, "is not prime number")

# /////////////////////////////////////////////////////////////////////

#  Write a Python function that calculates the factorial of a number.

def factorial(num) :
    if num < 0 :
        return None
    elif num == 0 :
        return 1
    else :
        prod = 1;
        for i in range (1, num+1) :
            prod *= i
        return prod

fact =  factorial(num)
if fact is None :
    print("Factorial of number less than 0 is undefined")
else :
    print("factorial of ", num , "is", fact)

# ///////////////////////////////////////////////////////////////

# Use list comprehension to create a list of the squares of the numbers from 1 to 10.

squared_list = [i**2 for i in range(1,11)]
# for i in range(1,11):
#     squared_list.append(i*i)
print("list of square of numbers from 1-10 : ", squared_list)