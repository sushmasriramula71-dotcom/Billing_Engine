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


def employee_statistics(result):
    if len(result) == 0:
        print("No records found")
        return

    total_salary = 0
    highest = result[0]
    lowest = result[0]
    department_count = {}

    for e in result:
        total_salary += e["salary"]

        if e["salary"] > highest["salary"]:
            highest = e

        if e["salary"] < lowest["salary"]:
            lowest = e

        department = e["department"]

        if department in department_count:
            department_count[department] += 1
        else:
            department_count[department] = 1

    print("\nTotal Employees:", len(result))
    print("Total Monthly Salary:", total_salary)
    print("Highest-Paid Employee:", highest["name"], highest["salary"])
    print("Lowest-Paid Employee:", lowest["name"], lowest["salary"])
    print("\nDepartment-Wise Count:")

    for department, count in department_count.items():
        print(department, ":", count)


def display_employees(result):
    if len(result) == 0:
        print("No records found")
        return

    for e in result:
        print(e)

    employee_statistics(result)


def multi_field_search():
    term = input("Enter Search Term: ").strip().lower()
    result = []

    for e in employees:
        if term in e["name"].lower() or term in e["department"].lower():
            result.append(e)

    display_employees(result)


def filtered_search():
    department = input("Enter Department (empty for all): ").strip()

    try:
        min_salary = int(input("Enter Minimum Salary: "))
        max_salary = int(input("Enter Maximum Salary: "))
        min_experience = int(input("Enter Minimum Experience: "))

        if min_salary < 0 or max_salary < 0 or min_experience < 0:
            print("Negative values not allowed")
            return

        if min_salary > max_salary:
            print("Invalid Salary Range")
            return

        result = []

        for e in employees:
            if department and e["department"].lower() != department.lower():
                continue

            if e["salary"] < min_salary or e["salary"] > max_salary:
                continue

            if e["experience"] < min_experience:
                continue

            result.append(e)

        display_employees(result)

    except ValueError:
        print("Enter Numeric Values Only")


def experience_status_search():
    print("1. Fresher")
    print("2. Experienced")
    print("3. Senior")

    choice = input("Enter Choice: ")
    result = []

    if choice == "1":
        for e in employees:
            if e["experience"] == 0 or e["experience"] == 1:
                result.append(e)

    elif choice == "2":
        for e in employees:
            if e["experience"] > 1:
                result.append(e)

    elif choice == "3":
        for e in employees:
            if e["experience"] >= 5:
                result.append(e)

    else:
        print("Invalid Choice")
        return

    display_employees(result)


def best_match_search():
    term = input("Enter Employee Name: ").strip().lower()

    if not term:
        print("Search term cannot be empty")
        return

    exact = []
    starts = []
    contains = []

    for e in employees:
        name = e["name"].lower()

        if name == term:
            exact.append(e)
        elif name.startswith(term):
            starts.append(e)
        elif term in name:
            contains.append(e)

    groups = [exact, starts, contains]

    for group in groups:
        n = len(group)

        for i in range(n):
            for j in range(n - i - 1):
                if group[j]["salary"] > group[j + 1]["salary"]:
                    group[j], group[j + 1] = group[j + 1], group[j]

    result = exact + starts + contains
    display_employees(result)


while True:
    print("\n===== Employee Management System =====")
    print("1. Multi-Field Search")
    print("2. Filtered Search")
    print("3. Experience Status Search")
    print("4. Best Match Search")
    print("5. All Employee Statistics")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        multi_field_search()
    elif choice == "2":
        filtered_search()
    elif choice == "3":
        experience_status_search()
    elif choice == "4":
        best_match_search()
    elif choice == "5":
        display_employees(employees)
    elif choice == "6":
        print("Exiting Employee Management System")
        break
    else:
        print("Invalid Choice")
