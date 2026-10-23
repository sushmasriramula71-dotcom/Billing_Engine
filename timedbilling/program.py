import csv
from datetime import datetime,timedelta
plans={}
with open("plans.csv","w") as f1:
    f1.write("""plan_code,monthly_fee,included_units
BASIC,499.00,10000
PRO,1499.00,50000
SCALE,3999.00,200000
""")
    
with open("plans.csv","r") as plan:
    cont=csv.DictReader(plan)
    for line in cont:
        plans[line["plan_code"]]={"monthly_fee":line["monthly_fee"],"included_units":int(line["included_units"])}
print(plans)


with open("subscription.csv","w") as subscription:
    subscription.write("""customer_id,event_date,event_type,plan_code
C001,2025-11-01,START,BASIC
C002,2026-09-16,START,PRO
C003,2025-02-01,START,BASIC
C003,2026-09-11,CHANGE,PRO
C004,2024-06-01,START,SCALE
C004,2026-09-21,CHANGE,BASIC
C005,2025-08-01,START,PRO
C005,2026-09-14,CANCEL,
C006,2026-09-05,START,BASIC
C006,2026-09-21,CANCEL,
C007,2024-01-01,START,BASIC
C007,2026-08-20,CANCEL,
""")

    
events={}
with open("subscription.csv","r") as sub:
    content=csv.DictReader(sub)
    for i in content:
        customer=i["customer_id"]
        if customer not in events:
            events[customer]=[]
        events[customer].append(i)
for customer in events:
    print(customer,events[customer])
for customer in events:
    cust=events[customer]
    for i in range(len(cust)):
        for j in range(i+1,len(cust)):
            if cust[i]["event_date"]>cust[j]["event_date"]:
                temp=cust[i]
                cust[i]=cust[j]
                cust[j]=temp
print("after sort")
for customer in events:
    print(customer,events[customer])


month_start=datetime.strptime("2026-09-01","%Y-%m-%d")
month_end=datetime.strptime("2026-09-30","%Y-%m-%d")
billing_month="2026-09"
segments={}
for customer in events:
    cust=events[customer]
    plan=""
    start_date=None
    segments[customer]=[]
    for event in cust:
        date=datetime.strptime(event["event_date"],"%Y-%m-%d")
        event_type=event["event_type"]
        if event_type=="START":
            plan=event["plan_code"]
            start_date=date
        elif event_type=="CHANGE" or event_type=="CANCEL":
            if plan!="":
                if event_type=="CHANGE":
                    end_date=date-timedelta(days=1)
                else:
                    end_date=date
                first=start_date
                last=end_date
                if first<month_start:
                    first=month_start
                if last>month_end:
                    last=month_end
                if first<=last and start_date<=month_end and end_date>=month_start:
                    segments[customer].append({"plan_code":plan,"start_date":first.strftime("%Y-%m-%d"),"end_date":last.strftime("%Y-%m-%d")})
            if event_type=="CHANGE":
                plan=event["plan_code"]
                start_date=date
            else:
                plan=""
                start_date=None
    if plan!="" and start_date<=month_end:
        first=start_date
        if first<month_start:
            first=month_start
        segments[customer].append({"plan_code":plan,"start_date":first.strftime("%Y-%m-%d"),"end_date":month_end.strftime("%Y-%m-%d")})
print("Generated Segments:")
for customer in segments:
    print(customer,segments[customer])
for customer in segments:
    for segment in segments[customer]:
        start_date=datetime.strptime(segment["start_date"],"%Y-%m-%d")
        end_date=datetime.strptime(segment["end_date"],"%Y-%m-%d")
        days=(end_date-start_date).days+1
        segment["days"]=days
        plan=segment["plan_code"]
        units=plans[plan]["included_units"]
        included_units=int(units*days/30)
        segment["included_units"]=included_units
print("Segments with Days and Units:")
for customer in segments:
    print(customer,segments[customer])
for customer in segments:
    for segment in segments[customer]:
        plan=segment["plan_code"]
        monthly_fee=float(plans[plan]["monthly_fee"])
        days=segment["days"]
        fee=round(monthly_fee*days/30,2)
        segment["fee"]=format(fee,".2f")
print("Segments with Fees:")
for customer in segments:
    print(customer,segments[customer])
customer_summary={}
for customer in segments:
    if len(segments[customer])>0:
        active_days=0
        total_fee=0
        for segment in segments[customer]:
            active_days+=segment["days"]
            total_fee+=float(segment["fee"])
        customer_summary[customer]={"active_days":active_days,"total_fee":format(round(total_fee,2),".2f")}
print("Customer Summary:")
print(customer_summary)
customer_count=0
segment_count=0
customers_without_segments=0
total_fee=0
for customer in segments:
    if len(segments[customer])>0:
        customer_count+=1
        for segment in segments[customer]:
            segment_count+=1
            total_fee+=float(segment["fee"])
    else:
        customers_without_segments+=1
summary={"customer_count":customer_count,"segment_count":segment_count,"customers_without_segments":customers_without_segments,"total_fee":format(round(total_fee,2),".2f")}
print("Billing Summary:")
print(summary)
plan_totals={}
for customer in segments:
    for segment in segments[customer]:
        plan=segment["plan_code"]
        if plan not in plan_totals:
            plan_totals[plan]={"segment_count":0,"total_fee":0}
        plan_totals[plan]["segment_count"]+=1
        plan_totals[plan]["total_fee"]+=float(segment["fee"])
print("Plan Totals:")
for plan in plan_totals:
    print({"plan_code":plan,"segment_count":plan_totals[plan]["segment_count"],"total_fee":format(round(plan_totals[plan]["total_fee"],2),".2f")})


import pyodbc
conn=pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=ACU-HYD-LT-2011\\SQLEXPRESS;"
    "Database=you;"
    "Trusted_Connection=yes;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)
cur=conn.cursor()
cur.execute("""
CREATE TABLE dbo.billing_segments(
    billing_month VARCHAR(7),
    customer_id VARCHAR(50),
    plan_code VARCHAR(20),
    start_date DATE,
    end_date DATE,
    days INT,
    fee DECIMAL(10,2),
    included_units INT)""")
conn.commit()

cur.execute("DELETE FROM dbo.billing_segments WHERE billing_month=?",(billing_month,))
for customer in segments:
    for segment in segments[customer]:
        cur.execute("""INSERT INTO dbo.billing_segments(
            billing_month,customer_id,plan_code,start_date,end_date,days,fee,included_units) VALUES(?,?,?,?,?,?,?,?)\
            """,(billing_month,customer,segment["plan_code"],segment["start_date"],segment["end_date"],segment["days"],segment["fee"],segment["included_units"]))
conn.commit()
cur.execute("""SELECT customer_id,plan_code,start_date,end_date,days,fee,included_units FROM dbo.billing_segments WHERE billing_month=? ORDER BY customer_id,start_date""",(billing_month,))
for row in cur.fetchall():
    print(row)
cur.close()
conn.close()

