# ython Project: Employee Management System
# Topics: Lists, dictionaries, functions, searching, filtering, validation, Bubble Sort, and statistics.
# Given data
# employees = [    {"id": 101, "name": "Arjun", "department": "IT", "salary": 75000, "experience": 3},    {"id": 102, "name": "Divya", "department": "HR", "salary": 45000, "experience": 2},    {"id": 103, "name": "Rahul", "department": "IT", "salary": 60000, "experience": 4},    {"id": 104, "name": "Priya", "department": "Finance", "salary": 55000, "experience": 3},    {"id": 105, "name": "Kiran", "department": "HR", "salary": 35000, "experience": 1},    {"id": 106, "name": "Sneha", "department": "IT", "salary": 90000, "experience": 5},    {"id": 107, "name": "Vijay", "department": "Finance", "salary": 40000, "experience": 2},    {"id": 108, "name": "Anjali", "department": "IT", "salary": 50000, "experience": 1}]
# Requirements
# 1. Multi-Field Search

# Search employees by name or department. The search should be case-insensitive.

# 2. Filtered Search

# Ask the user for department, minimum salary, maximum salary, and minimum experience.
# - Empty department means all departments.
# - Salary must be within the given range.
# - Experience must be greater than or equal to the minimum experience.
# - Reject negative values and invalid salary ranges.
# 3. Experience Status Search
# - 1 — Fresher: experience is 0 or 1 year.
# - 2 — Experienced: experience is greater than 1 year.
# - 3 — Senior: experience is greater than or equal to 5 years.
# 4. Best Match Search

# Search by employee name in this priority:
# - Exact name match
# - Names starting with the search term
# - Names containing the search term
# Sort each group by salary in ascending order using Bubble Sort. Do not use sort() or sorted().

# 5. Employee Statistics

# For the matching employees, display:
# - Total matching employees
# - Total monthly salary expenditure
# - Highest-paid employee
# - Lowest-paid employee
# - Department-wise employee count
# 6. Main Menu

# Repeat the menu until the user chooses Exit. Handle invalid menu choices and invalid numeric inputs.

employees = [
    {"id": 101, "name": "Arjun", "department": "IT", "salary": 75000, "experience": 3},
    {"id": 102, "name": "Divya", "department": "HR", "salary": 45000, "experience": 2},
    {"id": 103, "name": "Rahul", "department": "IT", "salary": 60000, "experience": 4},
    {"id": 104, "name": "Priya", "department": "Finance", "salary": 55000, "experience": 3},
    {"id": 105, "name": "Kiran", "department": "HR", "salary": 35000, "experience": 1},
    {"id": 106, "name": "Sneha", "department": "IT", "salary": 90000, "experience": 5},
    {"id": 107, "name": "Vijay", "department": "Finance", "salary": 40000, "experience": 2},
    {"id": 108, "name": "Anjali", "department": "IT", "salary": 50000, "experience": 1}
]

#  For the matching employees, display:
# # - Total matching employees
# # - Total monthly salary expenditure
# # - Highest-paid employee
# # - Lowest-paid employee
# # - Department-wise employee count
def employee_statistics(result):
    for e in employees:
        total_emps=0
        total_salary=0
        highest=employees[0]
        lowest=employees[0]
        dept_count={}

        for i in result:
            total_emps+=1

        for i in result:
            total_salary+=i['salary']

        for i in result:
            if i['salary']>highest:
                highest=i["salary"]

        for i in result:
            if i['salary']<lowest:
                lowest=i['salary']

        for i in result:
            depart=i['department']
            if depart in dept_count:
                dept_count['depart']+=1
            else:
                dept_count["depart"]=1

    print("total emps:", total_emps)
    print("total sal: ",total_salary)
    print("highest sal: ",highest)
    print("lowest sal: ",lowest)
    print("departmentcount: ",dept_count)

def display(result):
    if len(result)==0:
        print("no records found")
    else:
        for i in result:
            print(i)

# 1. Multi-Field Search
# Search employees by name or department. The search should be case-insensitive.
def multi_field_search():
    term=input('enter term').strip().lower()
    result=[]
    for e in employees:
        name=e['name'].lower()
        dept=e['department'].lower()
        if term in name or term in dept:
            result.append(e)
    display(result)

# 2. Filtered Search

# Ask the user for department, minimum salary, maximum salary, and minimum experience.
# - Empty department means all departments.
# - Salary must be within the given range.
# - Experience must be greater than or equal to the minimum experience.
# - Reject negative values and invalid salary ranges.
#
# 4. Best Match Search

def filtered_search():
    try:
        result=[]
        dept=input("Enter dept")
        min_sal=int(input("Enter minsal"))
        max_sal=int(input("Enter maxsal"))
        min_exp=int(input("enter exp"))

        if min_sal < 0 and max_sal < 0 and min_exp<0:
            print("values should be positive")
            return
        if min_sal>max_sal:
            print("invalid salary")
            return
        for e in employees:
            if dept!=e['department'].lower() and dept:
                continue
            if e['salary']<min_sal or e['salary']>max_sal:
                continue
            if e['experience']<min_exp:
                continue
            result.append(e)
        display(result)
    except Exception :
        print("Enter numeric values")

#3. Experience Status Search
# - 1 — Fresher: experience is 0 or 1 year.
# - 2 — Experienced: experience is greater than 1 year.
# - 3 — Senior: experience is greater than or equal to 5 years.
def exp_status_search():
    print("1.Fresher")
    print("2.Experienced")
    print("3.Senior")
    choice=input("enter choice:")
    if choice =="1":
        result=[]
        for e in employees:
            if e['experience']==0 or e['experience']==1:
                result.append(e)
            if e["experience"] >1:
                result.append(e)
            if e['experience']>=5:
                result.append(e)
    display(result)


def best_match_search():
    exact=[]
    starts=[]
    contains=[]
    term=input("enter term to match:").lower()
    for e in employees:
        name=e['names'].lower()
        if term == name:
            exact.append(e)
        if name.startswith(term):
            starts.append(e)
        if term in name:
            contains.append(e)
    groups=[exact,starts,contains]

    for group in groups:
        for i in range(len(groups)):
            for j in range(len(groups)-i-1):
                if group[j]['salary']>group[j+1]['salary']:
                    group[j]['salary'],group[j+1]['salary']=group[j+1]['salary'],group[j]['salary']
    result=exact+starts+contains
    display(result)

while True:
    print("1.Multi-field search")
    print("2.Filtered Search")
    print("3.experienced status search")
    print("4.Best match search")
    print("5.All employee staus")
    print("6.Exit")
    choice=input("enter choice")
    if choice=='1':
        multi_field_search()
    elif choice=='2':
        filtered_search()
    elif choice=='3':
        exp_status_search()
    elif choice=='4':
        best_match_search()
    elif choice=='5':
        employee_statistics()
    elif choice=='6':
        print("Emplo")
        break
    else:
        print("invalid choice1")


        
