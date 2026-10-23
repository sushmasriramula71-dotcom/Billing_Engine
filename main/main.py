from abc import ABC, abstractmethod
from datetime import date,datetime
import csv
class Loan:
    def __init__(self,loanid,member,book,borrow_date,return_date,book_condition):
        self.loanid=loanid
        self.member=member
        self.book=book
        self.borrow_date=borrow_date
        self.return_date=return_date
        self.book_condition=book_condition

    @abstractmethod
    def late_fine(self):
        pass
    def days_kept(self):
        if self.return_date is None:
            self.return_date=date.today()
        return (self.return_date-self.borrow_date).days
        
    def late_days(self):
        if self.days_kept>self.free_days:
            return self.days_kept() - self.free_days
        else:
            return 0   
    def extra_charge(self,damaged_book_percent,lost_book_percent):
        if self.book_condition=='Good':
            return 0
        elif self.book_condition=='Damaged':
            return self.book.price*self.damaged_book_percent/100
        elif self.book_condition=='Lost':
            return self.book.price*self.lost_book_percent/100

    def total_fine(self):
        return self.extra_charge(self.damaged_book_percent,self.lost_book_percent)+self.late_fine()
    def status(self):
        if self.return_date is None:
            return "Not Returned"
        return "Returned"
class StudentLoan(Loan):
    def __init__(self, loanid, member, book, borrow_date, return_date, book_condition):
        super().__init__(loanid, member, book, borrow_date, return_date, book_condition)
    def late_days(self):
        return self.late_days()*self.fine_per_day
class TeacherLoan(Loan):
    def __init__(self, loanid, member, book, borrow_date, return_date, book_condition,extra_grace_days):
        super().__init__(loanid, member, book, borrow_date, return_date, book_condition)
        self.extra_grace_days = extra_grace_days

    def  late_days(self):
        days=super.late_days()
        if days>self.extra_grace_days:
            return self.late_days-self.extra_grace_days
        else:
            return 0

class PublicLoan(Loan):
    def late_days(self):
        return super().late_days()
    def create_loan(abcd):
        loan_types={'student':StudentLoan,'teacher':TeacherLoan}
        loan_class = loan_types.get(abcd.lower())
        if loan_class is None:
            raise ValueError("Invalid member type")     
        return loan_class()
#     loans = [create_loan("Student"),create_loan("Teacher")]

#     for loan in loans:
#         print(loan.late_fine())
# loan = StudentLoan('loanid','member','book','borrow_date','return_date','book_condition')

with open("members.csv","w") as f:
    f.write("""MemberID,MemberName,MemberType,JoinDate
M01,Anil Reddy,Student,2024-06-10
M02,Sunita Rao,Teacher,2019-07-01
M03,Rahul Verma,Public,2023-02-15
M04,Kavya Nair,Student,2025-01-20
M05,Imran Shaikh,Public,2022-11-05
M06,,Student,2024-08-12
M07,Deepak Jain,Guest,2023-03-30
M03,Rahul V,Public,2023-02-15
M08,Meena Kumari,Teacher,2027-05-01
""")
member_types={"Student": { "free_days": 14, "fine_per_day": 2, "max_books": 3, "max_fine": 200 },"Teacher": { "free_days": 30, "fine_per_day": 1, "max_books": 5, "extra_grace_days": 5 },"Public":  { "free_days": 7,  "fine_per_day": 5, "max_books": 2, "double_after_days": 30 }}
memberids=set()
members=[]
with open("members.csv",'r') as f:
    cont=csv.DictReader(f,skipinitialspace=True)
   
    try:
        for line in cont:
            memberid=line['MemberID'].strip()
            membername=line['MemberName'].strip()
            membertype=line['MemberType'].strip()
            joindate=line['JoinDate'].strip()
            memberids.add(memberid)
            members.append(membername)


# MemberID must be present and must not repeat. Reject every repeat after the first one.
# MemberName must not be empty.
# MemberType must be one of the types listed in rules.json.
# JoinDate must be a correct date in YYYY-MM-DD format and must not be in the future.

        if not memberid and not membername and not membertype and not joindate:
            raise ValueError("Required fields are missing")
        # MemberType must be one of the types listed in rules.json.
        if membertype not in member_types:
            raise ValueError("membertype is not valid")
        try:
            datetime.strptime(joindate, "%Y-%m-%d")
        except ValueError:
            raise ValueError("JoinDate must be in YYYY-MM-DD format")
    except(KeyError,ValueError) as e:
        with open("error.txt",'w')as f2:
            f2.write(f"{line}-{e}\n")
    for i in members:
        print(i.memberid,i.membername,i.membertype,i.joindate)

with open("books.csv",'w') as f1:
    f1.write("""BookID,BookTitle,BookPrice
B01,Python Basics,450
B02,Data Structures,600
B03,World History,320
B04,English Grammar,0
B05,Science Facts,abc
B06,Short Stories,250
B07,Travel Guide,500
B08,,380
B01,Python Basics Second Edition,500
B09,Maths Puzzles,275
B10,Cooking Made Easy,350
""")
books=[]
bookids=set()
with open("books.csv",'r') as f1:
    cont=csv.DictReader(f1,skipinitialspace=True)
    try:
        for line in cont:
            bookid=line[0]
            booktitle=line[1]
            bookprice=int(line[2])
            bookids.add(bookid)
            books.append(booktitle)

# BookID must be present and must not repeat.
# BookTitle must not be empty.
# BookPrice must be a number and must be greater than zero.


        if not bookid and not booktitle and not bookprice:
            raise ValueError("required values are missing")
        if bookid in bookids:
            raise ValueError("bookid is duplicated")
        if bookprice<0:
            raise ValueError("bookprice must be greater than 0")
    except(ValueError,KeyError) as e:
        with open('error.txt','a') as f2:
            f2.write(f"{line}-{e}")
for i in books:
        print(i.bookid,i.booktitle,i.bookprice,i.bookids,i.books)


with open("loans.csv",'w') as f3:
    f3.write("""LoanID,MemberID,BookID,BorrowDate,ReturnDate,BookCondition
L01,M01,B03,2026-01-01,2026-05-25,Good
L02,M03,B01,2026-05-01,2026-07-20,Damaged
L03,M01,B07,2026-05-01,2026-05-10,Good
L04,M01,B02,2026-06-01,2026-07-15,Good
L05,M02,B07,2026-07-01,2026-08-04,Good
L06,M02,B09,2026-07-10,2026-09-20,Good
L07,M03,B10,2026-08-01,2026-08-20,Good
L08,M05,B03,2026-08-01,,Good
L09,M05,B06,2026-08-05,,Good
L10,M05,B09,2026-08-10,,Good
L11,M01,B10,2026-09-01,,Good
L12,M04,B02,2026-09-15,2026-09-25,Lost
L13,M01,B02,2026-10-01,,Good
L14,M09,B01,2026-09-01,,Good
L15,M01,B99,2026-09-05,,Good
L16,M01,B01,2027-01-10,,Good
L17,M04,B03,2024-05-01,2024-05-20,Good
L18,M02,B01,2026-09-01,2026-08-01,Good
L19,M03,B01,2026-09-10,2026-09-20,Broken
L20,M05,B01,bad-date,,Good
L21,M01,B03,2026-09-12,,Lost
L01,M02,B01,2026-09-02,,Good
""") 

loans=[]
loanids=set()
with open("loans.csv",'r') as f3:
    cont=csv.DictReader(f,skipinitialspace=True)
    try:
        
        for line in cont:
            loanid=line[0].strip()
            memberid=line[1].strip()
            bookid=line[2].strip()
            borrowdate=line[3].strip()
            returndate=line[4].strip()
            bookcondition=line[5].strip()
            loanids.add(loanid)

# LoanID must be present and must not repeat.
# MemberID must belong to a member that was accepted from members.csv.
# BookID must belong to a book that was accepted from books.csv.
# BorrowDate must be a correct date, must not be in the future, and must not be before the date the member joined.

        if not loanid and not memberid and not bookid and not borrowdate and not returndate and not bookcondition:
            raise ValueError("Required fields are missing")
        if memberid not in memberids:
            raise ValueError("memberid duplicated")
        if bookid not in bookids:
            raise ValueError("bookid is invalid")
        try:
            borrow_date = datetime.strptime(borrowdate, "%Y-%m-%d").date()
            join_date = datetime.strptime(joindate, "%Y-%m-%d").date()

            if borrow_date > date.today():
                raise ValueError("BorrowDate not be in the future")

            if borrow_date < join_date:
                raise ValueError("BorrowDate must not be before JoinDate")
# ReturnDate may be blank. When it is given, it must be a correct date, 
# must not be before the borrow date, and must not be in the future.
# BookCondition must be Good, Damaged or Lost.
# A book marked Damaged or Lost must have a return date, because the condition is known only when the book comes back or is reported.
        except(ValueError,KeyError) as e:
            with open("error.txt",'a') as f1:
                f1.write(f"{line}-{e}")
# BookCondition must be Good, Damaged or Lost.
# A book marked Damaged or Lost must have a return date, because the condition is known only when the book comes back or is reported.
        if bookcondition not in ["Good", "Damaged", "Lost"]:
            raise ValueError("book condition invalid")

        if bookcondition in ["Lost","Damaged"] and not returndate:
            raise ValueError("returned date is required for lost or damaged")
        print()
    except(ValueError,KeyError) as e:
        with open("error.txt",'a') as f2:
            f2.write(f"{line}={e}") 
for i in loans:
        print(i.loanid,i.memberid,i.bookid,i.borrowdate,i.returndate,i.bookcondition)


with open("rules.json",'w') as f3:
    f3.write("""{
  "member_types": {
    "Student": { "free_days": 14, "fine_per_day": 2, "max_books": 3, "max_fine": 200 },
    "Teacher": { "free_days": 30, "fine_per_day": 1, "max_books": 5, "extra_grace_days": 5 },
    "Public":  { "free_days": 7,  "fine_per_day": 5, "max_books": 2, "double_after_days": 30 }
  },
  "damaged_book_percent": 20,
  "lost_book_percent": 100
}""")

# with open("rules.json",'r') as f3:
#     cont=json.load(f3)

    





        


