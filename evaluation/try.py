def check_palindrome (num) :
    lst = []
    while num > 0 :
        rem = num%10
        lst.append(rem)
        num = int(num/10)
    # print(lst)
    for i in range(len(lst)) :
        if lst[i] != lst[len(lst)-1-i] :
            return False
    return True

print(check_palindrome(565))