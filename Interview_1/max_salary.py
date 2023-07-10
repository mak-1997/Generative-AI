def max_salry_employee (employees) :
    max_salary = 0
    out = {}
    for emp in employees :
        if emp["salary"] > max_salary :
            max_salary = emp["salary"]
            out = emp
    return out

employees = [
    { "name" : "sdfs", "salary" : 1000, "designation" : "devloper"},
    { "name" : "hjklhjl", "salary" : 5000, "designation" : "devloper"},
    { "name" : "dfgsdg", "salary" : 2500, "designation" : "dfgd"},
    { "name" : "jlyhl", "salary" : 3000, "designation" : "jk"},
]

print(max_salry_employee(employees))
