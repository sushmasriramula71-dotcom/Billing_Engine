# Question 6: Hotel Booking and Billing System
# Difficulty: Intermediate–Advanced · Time: 90 minutes
# Problem statement
# A hotel wants to process room bookings, calculate bills and apply eligible discounts.
# bookings = [{"booking_id": "B101", "customer": "Arun",     "room_type": "Deluxe", "nights": 3, "guests": 2,     "booking_date": "2026-10-10", "checkout_date": "2026-10-13"},    {"booking_id": "B102", "customer": "Divya",     "room_type": "Standard", "nights": 2, "guests": 1,     "booking_date": "2026-10-15", "checkout_date": "2026-10-17"},    {"booking_id": "B103", "customer": "Kiran",     "room_type": "Suite", "nights": 4, "guests": 3,     "booking_date": "2026-10-18", "checkout_date": "2026-10-22"},    {"booking_id": "B104", "customer": "Meena",     "room_type": "Deluxe", "nights": 1, "guests": 2,     "booking_date": "2026-10-20", "checkout_date": "2026-10-21"}]
# Room rates
# - Standard: ₹2,000 per night.
# - Deluxe: ₹3,500 per night.
# - Suite: ₹6,000 per night.
# - Bookings of at least three nights receive a 10% discount on room charges.
# - Bookings for more than two guests incur an additional ₹500 per night.


# Functional requirements
# 1. Calculate room charges, extra guest charges, discounts and final bills.
# 2. Create a base RoomBooking class and subclasses for different room types.
# 3. Use polymorphism for room charge calculation.
# 4. Validate booking IDs, customer names, room types, guest counts, nights and dates.
# 5. Reject duplicate booking IDs and invalid date ranges.
# 6. Search bookings by customer, room type, booking date and bill range.
# 7. Rank bookings by final bill descending, nights descending and customer name ascending.
# 8. Calculate total hotel revenue, total bookings and average bill.
# 9. Identify the most popular room type and highest-value booking.
# 10. Read bookings from bookings.csv and generate booking_report.csv.
# 11. Log rejected records in errors.txt.
# Additional challenge: Generate a date-wise booking summary and identify days with the highest number of check-ins.

class Roombooking:
    def __init__(self,booking_id,customer,room_type,nights,guests,booking_date,checkout_date):
        self.booking_id=booking_id
        self.customer=customer
        self.room_type=room_type
        self.nigths=nights
        self.guests=guests
        self.booking_date=booking_date
        self.checkout_date=checkout_date

    def charge_calculation(self,charge,rate):
        room_charge=self.rate*self.nights
        extra_guest_charge=0
        if self.guests>2:
            extra_guest_charge=500*self.nigths

        discount=0 
        if self.nigths>=3:
            discount=room_charge*0.10

        final_bill=room_charge+extra_guest_charge-discount
        return final_bill

class Standard(Roombooking):
    def __init__(self, booking_id, customer, room_type, nights, guests, booking_date, checkout_date):
        super().__init__(booking_id, customer, room_type, nights, guests, booking_date, checkout_date)

    def charge_calculation(self,charge):
        self.rate=2000
        return final_bill

class Deluxe(Roombooking):
    def __init__(self, booking_id, customer, room_type, nights, guests, booking_date, checkout_date):
        super().__init__(booking_id, customer, room_type, nights, guests, booking_date, checkout_date)

    def charge_calculation(self, charge, rate):
        self.rate=3500
        return super().charge_calculation(charge, rate)

class Suite(Roombooking):
    def __init__(self, booking_id, customer, room_type, nights, guests, booking_date, checkout_date):
        super().__init__(booking_id, customer, room_type, nights, guests, booking_date, checkout_date)

    def charge_calculation(self, charge, rate):
        self.rate=6000
        return super().charge_calculation(charge, rate)






from datetime import datetime
import csv
from collections import Counter

class Roombooking:
    def __init__(self,booking_id,customer,room_type,nights,guests,booking_date,checkout_date):
        self.booking_id=booking_id
        self.customer=customer
        self.room_type=room_type
        self.nights=nights
        self.guests=guests
        self.booking_date=booking_date
        self.checkout_date=checkout_date

    def charge_calculation(self):
        room_charge=self.rate*self.nights
        extra_guest_charge=0
        if self.guests>2:
            extra_guest_charge=500*self.nights
        discount=0
        if self.nights>=3:
            discount=room_charge*0.10
        return room_charge+extra_guest_charge-discount

class Standard(Roombooking):
    def __init__(self,booking_id,customer,room_type,nights,guests,booking_date,checkout_date):
        super().__init__(booking_id,customer,room_type,nights,guests,booking_date,checkout_date)
        self.rate=2000

class Deluxe(Roombooking):
    def __init__(self,booking_id,customer,room_type,nights,guests,booking_date,checkout_date):
        super().__init__(booking_id,customer,room_type,nights,guests,booking_date,checkout_date)
        self.rate=3500

class Suite(Roombooking):
    def __init__(self,booking_id,customer,room_type,nights,guests,booking_date,checkout_date):
        super().__init__(booking_id,customer,room_type,nights,guests,booking_date,checkout_date)
        self.rate=6000

bookings=[
    {"booking_id":"B101","customer":"Arun","room_type":"Deluxe","nights":3,"guests":2,"booking_date":"2026-10-10","checkout_date":"2026-10-13"},
    {"booking_id":"B102","customer":"Divya","room_type":"Standard","nights":2,"guests":1,"booking_date":"2026-10-15","checkout_date":"2026-10-17"},
    {"booking_id":"B103","customer":"Kiran","room_type":"Suite","nights":4,"guests":3,"booking_date":"2026-10-18","checkout_date":"2026-10-22"},
    {"booking_id":"B104","customer":"Meena","room_type":"Deluxe","nights":1,"guests":2,"booking_date":"2026-10-20","checkout_date":"2026-10-21"}
]

room_classes={"Standard":Standard,"Deluxe":Deluxe,"Suite":Suite}
processed_bookings=[]
booking_ids=[]
errors=[]

for booking in bookings:
    try:
        booking_id=booking["booking_id"]
        customer=booking["customer"]
        room_type=booking["room_type"]
        nights=booking["nights"]
        guests=booking["guests"]
        booking_date=datetime.strptime(booking["booking_date"],"%Y-%m-%d").date()
        checkout_date=datetime.strptime(booking["checkout_date"],"%Y-%m-%d").date()

        if not booking_id.strip():
            raise ValueError("Booking ID cannot be empty")
        if booking_id in booking_ids:
            raise ValueError("Duplicate booking ID")
        if not customer.strip():
            raise ValueError("Customer name cannot be empty")
        if room_type not in room_classes:
            raise ValueError("Invalid room type")
        if type(nights)!=int or nights<=0:
            raise ValueError("Nights must be a positive integer")
        if type(guests)!=int or guests<=0:
            raise ValueError("Guests must be a positive integer")
        if checkout_date<=booking_date:
            raise ValueError("Invalid date range")
        if (checkout_date-booking_date).days!=nights:
            raise ValueError("Nights do not match dates")

        room=room_classes[room_type](booking_id,customer,room_type,nights,guests,str(booking_date),str(checkout_date))
        bill=room.charge_calculation()
        booking_ids.append(booking_id)
        processed_bookings.append({"booking_id":booking_id,"customer":customer,"room_type":room_type,"nights":nights,"guests":guests,"booking_date":str(booking_date),"checkout_date":str(checkout_date),"final_bill":bill})
    except (ValueError,KeyError,TypeError) as e:
        errors.append(f"{booking.get('booking_id','Unknown')}: {e}")

for i in range(len(processed_bookings)):
    for j in range(i+1,len(processed_bookings)):
        a=processed_bookings[i]
        b=processed_bookings[j]
        swap=False
        if a["final_bill"]<b["final_bill"]:
            swap=True
        elif a["final_bill"]==b["final_bill"]:
            if a["nights"]<b["nights"]:
                swap=True
            elif a["nights"]==b["nights"] and a["customer"]>b["customer"]:
                swap=True
        if swap:
            processed_bookings[i],processed_bookings[j]=processed_bookings[j],processed_bookings[i]

total_revenue=0
room_counts={}
checkin_counts={}

print("Booking Report")
for booking in processed_bookings:
    print(booking)
    total_revenue+=booking["final_bill"]
    room_type=booking["room_type"]
    if room_type not in room_counts:
        room_counts[room_type]=0
    room_counts[room_type]+=1
    date=booking["booking_date"]
    if date not in checkin_counts:
        checkin_counts[date]=0
    checkin_counts[date]+=1

total_bookings=len(processed_bookings)
average_bill=0
if total_bookings>0:
    average_bill=total_revenue/total_bookings

most_popular_room="None"
highest_count=0
for room_type in room_counts:
    if room_counts[room_type]>highest_count:
        highest_count=room_counts[room_type]
        most_popular_room=room_type

highest_value_booking=None
if processed_bookings:
    highest_value_booking=processed_bookings[0]

print("Total Revenue:",total_revenue)
print("Total Bookings:",total_bookings)
print("Average Bill:",round(average_bill,2))
print("Most Popular Room Type:",most_popular_room)
print("Highest Value Booking:",highest_value_booking)

customer_name=input("Enter customer name to search: ").strip().lower()
print("Customer Search:")
for booking in processed_bookings:
    if customer_name in booking["customer"].lower():
        print(booking)

search_room=input("Enter room type to search: ").strip().title()
print("Room Type Search:")
for booking in processed_bookings:
    if booking["room_type"]==search_room:
        print(booking)

search_date=input("Enter booking date (YYYY-MM-DD): ").strip()
print("Booking Date Search:")
for booking in processed_bookings:
    if booking["booking_date"]==search_date:
        print(booking)

try:
    min_bill=float(input("Enter minimum bill: "))
    max_bill=float(input("Enter maximum bill: "))
    print("Bill Range Search:")
    for booking in processed_bookings:
        if min_bill<=booking["final_bill"]<=max_bill:
            print(booking)
except ValueError:
    print("Invalid bill range")

print("Date-wise Check-ins:",checkin_counts)
highest_checkins=0
for date in checkin_counts:
    if checkin_counts[date]>highest_checkins:
        highest_checkins=checkin_counts[date]

print("Days with Highest Check-ins:")
for date in checkin_counts:
    if checkin_counts[date]==highest_checkins:
        print(date,highest_checkins)

with open("bookings.csv","w",newline="") as file:
    fields=["booking_id","customer","room_type","nights","guests","booking_date","checkout_date"]
    writer=csv.DictWriter(file,fieldnames=fields)
    writer.writeheader()
    writer.writerows(bookings)

with open("booking_report.csv","w",newline="") as file:
    fields=["booking_id","customer","room_type","nights","guests","booking_date","checkout_date","final_bill"]
    writer=csv.DictWriter(file,fieldnames=fields)
    writer.writeheader()
    writer.writerows(processed_bookings)

with open("errors.txt","w") as file:
    for error in errors:
        file.write(error+"\n")