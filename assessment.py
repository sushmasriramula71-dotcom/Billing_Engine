# Create an abstract base class named ExpenseClaim using
#  the abc module. It must hold the claim ID, 
# the employee, the claim date and 
# the converted INR amount, and
#  must declare an abstract method calculate_eligible_amount().
# Create three subclasses: TravelClaim, MealClaim and AccommodationClaim. 
# Each subclass must override calculate_eligible_amount() with its own rule.

import csv
import json
from datetime import datetime
from abc import ABC, abstractmethod
class ExpenseClaim:
    def __init__(self,claim_id,emp,claim_date,amount):
        self.claim_id=claim_id
        self.emp=emp
        self.claim_date=claim_date
        self.amount=amount

    @abstractmethod
    def calculate_eligible_amount(self,amount):
        pass
        

class TravelClaim(ExpenseClaim):
     def __init__(self, claim_id, emp, claim_date, amount):
          super().__init__(claim_id, emp, claim_date, amount)
     def  calculate_eligible_amount(self):
        return f"{amount:.2f}"

class MealClaim(ExpenseClaim):
     def __init__(self, claim_id, emp, claim_date, amount):
          super().__init__(claim_id, emp, claim_date, amount)
     def calculate_eligible_amount(self):
         return f"{amount * 0.20:.2f}"
        
         

class AccommodationClaim(ExpenseClaim):
     def __init__(self, claim_id, emp, claim_date, amount):
          super().__init__(claim_id, emp, claim_date, amount)
     def calculate_eligible_amount(self):
          return f"{amount*0.88+amount:.2f}"

grade_limits=[]

with open("policy.json","w") as f2:
     f2.write('''{
  "currency_rates": { "INR": 1.0, "USD": 83.5, "EUR": 90.0 },
  "receipt_required_above": 2000,
  "monthly_cap_per_employee": 25000,
  "grade_limits": {
    "G1": { "Travel": 3000,  "Meal": 500,  "Accommodation": 4000  },
    "G2": { "Travel": 6000,  "Meal": 800,  "Accommodation": 7000  },
    "G3": { "Travel": 10000, "Meal": 1200, "Accommodation": 12000 }
  }
}
''')

     
with open("policy.json",'r') as f2:
     contents=json.load(f2)
     for line in contents:
        currency_rates=line[0].strip()
        receipt_required_above=line[1].strip()
        monthly_cap_per_employee=line[2].strip()
        grade_limit=line[3].strip()
        grade_limits.append(grade_limit)


with open("employees.csv","w") as f1:
     f1.write("""EmpID,EmpName,Department,Grade,JoinDate
E101,Ravi Kumar,Sales,G3,2023-05-10
E102,Anita Sharma,Engineering,G2,2024-01-15
E103,John Mathew,Sales,G1,2022-08-01
E104,Priya Nair,Engineering,G3,2025-03-20
E105,Imran Khan,Finance,G2,2021-11-05
E106,,Marketing,G2,2024-07-19
E107,Meera Joshi,Finance,G5,2024-02-11
E103,Jonathan Mathew,Sales,G2,2022-08-01
E108,Arun Verma,Marketing,G1,bad-date
""")
employees=[]
employee_ids=set()
     
with open("employees.csv","r") as f1:
    content=csv.DictReader(f1,skipinitialspace=True)
    for line in content:
         empid=line['EmpID'].strip()
         empname=line['EmpName'].strip()
         Dept=line["Department"].strip()
         grade=line["Grade"].strip()
         joindate=line['JoinDate'].strip()

    try:
         if not empid and not empname and not Dept and not grade and not joindate:
              raise ValueError("Required fields are missing")
         if empid in employee_ids:
              raise ValueError("Dulpicate empid")
         
         if grade not in grade_limits:
              raise ValueError("grade is in grade limit")
         if joindate is not format('YYYY-MM-DD'):
              raise ValueError("date is not correct format")
         with open("errors.txt",'w') as f3:
                     writer=csv.writer(f3)
                     writer.writerows(['ClaimID','EmpID','ClaimType','ClaimDate','Amount','Currency','ReceiptAttached'])
         
    except(ValueError,KeyError )as e:
         
          with open("errors.txt",'w') as f3:
            f3.write
            writer.writerows(['ClaimID','EmpID','ClaimType','ClaimDate','Amount','Currency','ReceiptAttached'])
            error.txt.write(f"{line}-{e}\n")
for e in employees:
     print(emp['empid'])
          
    

       



# grade_limits= {"G1": { "Travel": 3000,  "Meal": 500,  "Accommodation": 4000  },
#                 "G2": { "Travel": 6000,  "Meal": 800,  "Accommodation": 7000  },
#                 "G3": { "Travel": 10000, "Meal": 1200, "Accommodation": 12000 }}


         
with open("claims.csv","w") as f:
     f.write("""ClaimID,EmpID,ClaimType,ClaimDate,Amount,Currency,ReceiptAttached
CL001,E101,Travel,2026-07-05,8500,INR,Yes
CL002,E101,Meal,2026-07-05,1500,INR,No
CL003,E101,Accommodation,2026-07-06,15000,INR,Yes
CL004,E102,Travel,2026-07-10,120,USD,Yes
CL005,E102,Meal,2026-07-10,400,INR,No
CL006,E103,Travel,2026-07-12,2500,INR,No
CL007,E103,Accommodation,2026-07-12,5000,INR,Yes
CL008,E104,Travel,2026-08-01,9000,INR,Yes
CL009,E104,Travel,2026-08-01,7000,INR,Yes
CL010,E104,Meal,2026-08-02,2200,INR,Yes
CL011,E105,Travel,2026-08-05,50,EUR,Yes
CL012,E105,Accommodation,2026-08-05,abc,INR,Yes
CL013,E109,Travel,2026-08-07,3000,INR,Yes
CL014,E102,Meal,2027-01-15,900,INR,Yes
CL015,E104,Travel,2024-12-01,5000,INR,Yes
CL016,E105,Travel,2026-08-09,4000,GBP,Yes
CL017,E101,Accommodation,2026-07-20,-3000,INR,Yes
CL001,E102,Travel,2026-08-11,2000,INR,Yes
CL018,E105,Meal,2026-08-12,700,INR,No
CL019,E101,Travel,2026-07-25,20000,INR,Yes
CL020,E101,Travel,2026-07-28,9000,INR,Yes
""")
with open("claims.csv",'r') as f:
     cont=csv.DictReader(f,skipinitialspace=True)
     for line in cont:
          claimid=line['ClaimID']
          empid=line["EmpID"]
          claim_type=line['ClaimType'].strip()
          claim_date=line['ClaimDate'].strip()
          amount=int(line['Amount'])
          currency=float(line['Currency'])
          receiptAttached=bool(line['ReceiptAttached'])
     e=ExpenseClaim('claim_id', 'emp', 'claim_date', 'amount')
     try:
          if not claimid and not empid and not claim_type and not claim_date and not amount and not currency and not receiptAttached:
               raise ValueError("Required Values are missing")
          

          if claimid in e.claim_id:
               raise ValueError("claimid not found")
          #EmpID must refer to an employee accepted from the employee master.

          if claim_type != 'Travel' or claim_type !='Meal' or claim_type !='Accommodation':
               raise ValueError("claim type is invalid")
          if claim_date is not format('YYYY-MM-DD'):
               raise ValueError("claim date is not of correct format")
          if amount<0:
               raise ValueError("Amount not be in negative")
        #   if currency not in currency_rates:currency = line['Currency']

          #  currency not in currency_rates.keys():
          #      raise ValueError("currency is not valid")
          # if (receiptAttached != 'Yes' or receiptAttached!= 'No') :
          #      raise ValueError("rejecting the claim")
          # print()
     except(ValueError,KeyError) as e:
          with open("errors.txt",'w') as f3:
               writer=csv.writer(f3)
               writer.writerow(['ClaimID','EmpID','ClaimType','ClaimDate','Amount','Currency','ReceiptAttached'])
          print(f"{line}-{e}\n")




          


          