def reverse_string (str) :
    rev = ""
    for i in range(0, len(str)) :
        rev += str[len(str)-1 - i]
    return rev

print(reverse_string("mayank singh"))
    