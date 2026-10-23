# Question 2: Student Examination Performance Analyzer
# Difficulty: Intermediate · Time: 90 minutes
# Problem statement
# A college wants to analyze student performance across Python, SQL and Web API subjects.
# students = [{"id": 201, "name": "Ravi", "python": 88,"sql": 76, "web_api": 91},    {"id": 202, "name": "Meena", "python": 65,     "sql": 82, "web_api": 70},    {"id": 203, "name": "Rahul", "python": 45,     "sql": 78, "web_api": 85},    {"id": 204, "name": "Anu", "python": 92,     "sql": 91, "web_api": 89},    {"id": 205, "name": "Kavya", "python": 70,     "sql": 70, "web_api": 70}]
# Functional requirements
# 1. Calculate total and average marks for every student.
# 2. A student passes only if every subject mark is at least 50.
# 3. Assign grades: Excellent (average ≥ 85), Good (average ≥ 70), otherwise Needs Improvement. A failed student must also be identified separately.
# 4. Rank students by average descending, Python marks descending and name ascending.
# 5. Display the top five students.
# 6. Identify the topper in each subject. Display all tied toppers.
# 7. Calculate subject-wise average, highest marks, lowest marks and pass percentage.
# 8. Find students whose average is below the class average.
# 9. Search by name, marks range, grade and pass/fail status.--------------
# 10. Validate marks from 0 to 100 and handle duplicate IDs and invalid records.
# Additional challenge: Display the number of students in each grade and the overall class performance summary.


students = [{"id": 201, "name": "Ravi", "python": 88,"sql": 76, "web_api": 91},    
            {"id": 202, "name": "Meena", "python": 65,"sql": 82, "web_api": 70},   
            {"id": 203, "name": "Rahul", "python": 45,"sql": 78, "web_api": 85},    
            {"id": 204, "name": "Anu", "python": 92,"sql": 91, "web_api": 89},    
            {"id": 205, "name": "Kavya", "python": 70,"sql": 70, "web_api": 70}]
total_marks=[]
avg_marks=[]
grades=[]
for s in students:
    total=s['python']+s['sql']+s['web_api']
    avgs=(s['python']+s['sql']+s['web_api'])/3
    s['total_marks']=total
    s['avg_marks']=avgs
    total_marks.append(total)
    avg_marks.append(avgs)
print("total_marks: ",total_marks,"\nAvgMarks: ",avg_marks)
# print("passedstudents:",passed_students)

for s in students:
    avg=(s['python']+s['sql']+s['web_api'])/3

    if avg>=85:
        grade="Excellent"
    elif avg>=70:
        grade="Good"
    else:
        grade="Needs Improvement"

    if s['python'] < 50 or s['sql'] < 50 or s['web_api'] < 50:
        status = "Fail"
    else:
        status = "Pass"
    s['grade']=grade
    s['status']=status
# print(s['name'],grade,status)

# Rank students by average descending, Python marks descending and name ascending.
swap=False
for i in range(len(students)):
    for j in range(len(students)-1-i):
        if students[j]['avg_marks']<students[j+1]['avg_marks']:
            swap=True
        elif students[j]['avg_marks']==students[j+1]['avg_marks']:
            if students[j]['python']<students[j]['python']:
                swap=True
            elif students[j].lower()>students[j+1].lower():
                swap=True
if swap:
    students[j],students[j+1]=students[j+1],students[j]
for s in students:
    print(s)


for sub in ["python","sql","web_api"]:
    highest=0
    lowest=0
    avg=0
    for s in students:
        if s[sub]>highest:
            highest=s[sub]
        if s[sub]<lowest:
            lowest=s[sub]
        avg+=s[sub]
    print(f"****{sub}****")
    print(s['name'],sub,highest)
    # print("lowset")
    print("Lowest: ",s['name'],sub,lowest)
    print("avg: ",sub,avg)
    # print(avg)


cls_avg=avgs/len(students)
for s in students:
    avg=(s['python']+s['sql']+s['web_api'])/3
    if cls_avg>avg:
        print(s['name'],avg)
    else:
        print("no students avg is lessthan clsavg")

for grade in ['Excellent' ,'Good', 'Needs Improvement']:






# students = [{"id": 201, "name": "Ravi", "python": 88, "sql": 76, "web_api": 91},
#             {"id": 202, "name": "Meena", "python": 65, "sql": 82, "web_api": 70},
#             {"id": 203, "name": "Rahul", "python": 45, "sql": 78, "web_api": 85},
#             {"id": 204, "name": "Anu", "python": 92, "sql": 91, "web_api": 89},
#             {"id": 205, "name": "Kavya", "python": 70, "sql": 70, "web_api": 70}]
# total_marks=[]
# avg_marks=[]
# grades=[]
# valid_students=[]
# invalid_records=[]
# ids=[]

# for s in students:
#     if not all(k in s for k in ['id','name','python','sql','web_api']) or type(s.get('id'))!=int or not isinstance(s.get('name'),str) or not s.get('name','').strip() or s['id'] in ids or any(type(s.get(sub))!=int or not 0<=s[sub]<=100 for sub in ['python','sql','web_api']):
#         invalid_records.append(s)
#         continue
#     ids.append(s['id'])
#     total=s['python']+s['sql']+s['web_api']
#     avgs=total/3
#     s['total_marks']=total
#     s['avg_marks']=avgs
#     total_marks.append(total)
#     avg_marks.append(avgs)
#     valid_students.append(s)

# students=valid_students
# print("total_marks:",total_marks,"\nAvgMarks:",avg_marks)
# print("Invalid records:",invalid_records)

# for s in students:
#     avg=s['avg_marks']
#     if avg>=85:
#         grade="Excellent"
#     elif avg>=70:
#         grade="Good"
#     else:
#         grade="Needs Improvement"
#     if s['python']<50 or s['sql']<50 or s['web_api']<50:
#         status="Fail"
#     else:
#         status="Pass"
#     s['grade']=grade
#     s['status']=status

# print("\nStudent performance:")
# for s in students:
#     print(s['name'],s['total_marks'],round(s['avg_marks'],2),s['grade'],s['status'])

# swap=False
# for i in range(len(students)):
#     for j in range(len(students)-1-i):
#         swap=False
#         if students[j]['avg_marks']<students[j+1]['avg_marks']:
#             swap=True
#         elif students[j]['avg_marks']==students[j+1]['avg_marks']:
#             if students[j]['python']<students[j+1]['python']:
#                 swap=True
#             elif students[j]['python']==students[j+1]['python'] and students[j]['name'].lower()>students[j+1]['name'].lower():
#                 swap=True
#         if swap:
#             students[j],students[j+1]=students[j+1],students[j]

# print("\nRankings:")
# for i,s in enumerate(students,1):
#     print(i,s['name'],round(s['avg_marks'],2),s['python'])

# print("\nTop five students:")
# for s in students[:5]:
#     print(s['name'],round(s['avg_marks'],2))

# for sub in ["python","sql","web_api"]:
#     highest=max(s[sub] for s in students)
#     lowest=min(s[sub] for s in students)
#     avg=sum(s[sub] for s in students)/len(students)
#     passed=sum(1 for s in students if s[sub]>=50)
#     print(f"\n****{sub}****")
#     print("Highest:",highest)
#     print("Topper(s):",[s['name'] for s in students if s[sub]==highest])
#     print("Lowest:",lowest)
#     print("Average:",round(avg,2))
#     print("Pass percentage:",round(passed/len(students)*100,2),"%")

# cls_avg=sum(avg_marks)/len(avg_marks) if avg_marks else 0
# print("\nClass average:",round(cls_avg,2))
# print("Students below class average:")
# below_found=False
# for s in students:
#     if s['avg_marks']<cls_avg:
#         print(s['name'],round(s['avg_marks'],2))
#         below_found=True
# if not below_found:
#     print("No students")

# print("\nGrade counts:")
# for grade in ['Excellent','Good','Needs Improvement']:
#     count=0
#     for s in students:
#         if s['grade']==grade:
#             count+=1
#     print(grade,count)

# print("\nOverall class performance:")
# passed_students=[s for s in students if s['status']=="Pass"]
# failed_students=[s for s in students if s['status']=="Fail"]
# print("Total students:",len(students))
# print("Passed students:",[s['name'] for s in passed_students])
# print("Failed students:",[s['name'] for s in failed_students])
# print("Class pass percentage:",round(len(passed_students)/len(students)*100,2) if students else 0,"%")
# print("Class average:",round(cls_avg,2))

# print("\nSearch options: 1.Name 2.Marks range 3.Grade 4.Pass/Fail")
# choice=input("Enter choice:")
# result=[]

# if choice=='1':
#     name=input("Enter name:").strip().lower()
#     for s in students:
#         if name in s['name'].lower():
#             result.append(s)
# elif choice=='2':
#     low=int(input("Enter minimum marks:"))
#     high=int(input("Enter maximum marks:"))
#     if 0<=low<=high<=100:
#         for s in students:
#             if low<=s['python']<=high or low<=s['sql']<=high or low<=s['web_api']<=high:
#                 result.append(s)
#     else:
#         print("Invalid marks range")
# elif choice=='3':
#     grade=input("Enter grade:").strip().lower()
#     for s in students:
#         if s['grade'].lower()==grade:
#             result.append(s)
# elif choice=='4':
#     status=input("Enter Pass or Fail:").strip().lower()
#     for s in students:
#         if s['status'].lower()==status:
#             result.append(s)
# else:
#     print("Invalid choice")

# if result:
#     for s in result:
#         print(s)
# else:
#     print("No students found")





