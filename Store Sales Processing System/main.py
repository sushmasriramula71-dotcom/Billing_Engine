# Create an abstract base class Sale using the abc module, holding the
#  transaction id, the store, the timestamp, the product, 
# the quantity and the payment method, with an abstract method member_discount().
# Create two subclasses, MemberSale and GuestSale, each overriding member_discount().
# Pick the right subclass from the customer field using a dictionary, not a chain of if statements.
# Override __str__ so printing a sale gives one readable line.
# Create your own exceptions: a base SalesError with ValidationError below it.
# Custom Exceptions


import csv
import json
from decimal import Decimal, ROUND_HALF_UP
from abc import ABC, abstractmethod
class Sale:
    def __init__(self,transactionid,store,timestamp,product,quantity,paymentmethod):
        self.transactionid=transactionid
        self.store=store
        self.timestamp=timestamp
        self.product=product
        self.quantity=quantity
        self.paymentmethod=paymentmethod
    def money(self, amount):
        return amount.quantize(Decimal("0.01"),rounding=ROUND_HALF_UP)

    @abstractmethod
    def member_discount(self,gross):
        self.gross = self.money(self.product["price"] * self.quantity)
        tax_rate = tax_rates[self.product["category"]]
        tax = self.money(self.gross * tax_rate)
        discount = self.member_discount(gross)
        total = self.money(self.gross + tax - discount)
        return {"gross": self.gross,"tax": tax,
            "discount": discount,"total": total}
    def __str__(self):
        return (f"transactionid : {self.transactionid},store : {self.store}, timestamp : {self.timestamp}, product: {self.product}, quantity : {self.quantity}, paymentmethod : {self.paymentmethod}")

class MemberSale(Sale):
    def member_discount(self):
        discount = self.gross * self.member_discount_percent / Decimal("100")
        return self.money(discount)
        
class GuestSale(Sale):
    def member_discount(self):
        return self.money(Decimal("0.00"))

class SalesError(Exception):
    pass
class ValidationError(SalesError):
    pass

sale_classes = {"Member": MemberSale,"Guest": GuestSale}

def create_sale(transactionid, store, timestamp, product,
                quantity, payment_method, customer):

    sale_class = sale_classes.get(customer)
    if sale_class is None:
        raise ValidationError("Invalid customer type")
    return sale_class(
        transactionid,
        store,
        timestamp,
        product,
        quantity,
        payment_method,
        customer
    )
# payment_methods=[]
with open("products.json","r") as f:
    cont=json.load(f)
    for line in cont:
        catalogue=line[0]
        taxrates=line[1]
        memberdiscountpercent=line[2]
        payment_methods=line[3]

transactionids=set()
with open("sales.txt",'r') as f:
    cont=f.read()
    for line in cont:
        timestamp=line[0].strip()
        store=line[1].strip()
        transactionid=line[2].strip()
        product_quantity=line[3]
        payment_method=line[4].strip()
        customer=line[5].strip()
        transactionids.add(transactionid)
    try:
# The line must split into exactly six fields on the pipe character.
# The timestamp must match YYYY-MM-DD HH:MM:SS.-------------
# The transaction id must not repeat.
# The item must be in the form CODE x QTY, and the code must exist in the catalogue.--------
# The quantity must be a whole number from 1 to 50.-----------------
# The payment method must be one of the methods listed in products.json.
# The customer must be MEMBER or GUEST.
        if not timestamp and not store and not transactionid and not product_quantity and not payment_method and not customer:
            raise ValueError("Required fields are missing")
        if transactionid in transactionids:
            raise ValueError("transactionid is duplicated")
        if payment_method not in payment_methods:
            raise ValueError("payment method invalid")
        if customer not in ['MEMBER','GUEST']:
            raise ValueError("invalid customer")
    except(ValueError,KeyError) as e:
        with open("errors.txt",'w')as f1:
            f1.write(f"{line}={e}\n")

# Create a SQLite database named sales.db with two tables: products and sales. The sales table must have a foreign key to products.
# Insert using parameter placeholders, never by joining strings into the SQL.
# Run one query that joins the two tables and groups by category to give the revenue of each category, highest first.
import pyodbc
connention=pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
    "Server=ACU-HYD-LT-2011\\SQLEXPRESS;"
    "Database=master;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;")
cursor=connention.cursor()
cursor.execute("create database Sales;")
cursor.commit
connention1=pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
    "Server=ACU-HYD-LT-2011\\SQLEXPRESS;"
    "Database=Sales;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;")
cursor1=connention.cursor()
q1="create table products(code varchar(20) primary key,name varchar(20) not null," \
"category varchar(20) not null,price int not null);"
cursor.execute(q1)
q2="create table sales(timestamp time,store nvarchar(20),transact);"

        
# timestamp | store | transaction id | product x quantity | payment | customer