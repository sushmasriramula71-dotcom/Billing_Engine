# Date Difference Calculator

# Write a Python program that:
# 1. Takes two dates from the user in DD-MM-YYYY format.
# 2. Converts both strings into datetime objects.
# 3. Calculates the number of days between them.
# 4. Handles invalid dates using try-except.

# Example input:
# Enter first date: 23-10-2026
# Enter second date: 30-10-2026


from datetime import datetime, date
d1=date.today()
d2="30-10-2026"
d2=datetime.strptime(d2,"%d-%m-%Y").date()
diff=d2-d1
print(diff.days)

d3=datetime.now()
print(d3)
d9=datetime.strftime("%d-%m-%Y")
print(d9)

