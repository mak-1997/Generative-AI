company = {
    'employees': {
        'John': {'age': 35, 'job_title': 'Manager'},
        'Emma': {'age': 28, 'job_title': 'Software Engineer'},
        'Kelly': {'age': 41, 'job_title': 'Senior Developer'},
        'Sam': {'age': 30, 'job_title': 'Software Engineer'},
        'Mark': {'age': 37, 'job_title': 'Senior Manager'},
        'Sara': {'age': 32, 'job_title': 'Software Engineer'},
    }
}

def avg_age(data) :
    count = 0
    sum = 0
    for key,value in data["employees"] :
        # job = key["job_title"]
        print(key,value)
        # if job[0] == "S" :
        #     count += 1
        #     sum += key["age"]
    # return sum/count

print(avg_age(company))