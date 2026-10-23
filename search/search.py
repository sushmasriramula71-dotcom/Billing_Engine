products = [
    {"id": 101, "name": "Wireless Mouse", "category": "Accessories", "price": 850, "stock": 25, "min_stock": 10},
    {"id": 102, "name": "Gaming Mouse", "category": "Accessories", "price": 1800, "stock": 5, "min_stock": 10},
    {"id": 103, "name": "Mechanical Keyboard", "category": "Accessories", "price": 3200, "stock": 12, "min_stock": 5},
    {"id": 104, "name": "Laptop Pro 14", "category": "Computers", "price": 68000, "stock": 8, "min_stock": 3},
    {"id": 105, "name": "Laptop Air 13", "category": "Computers", "price": 55000, "stock": 0, "min_stock": 5},
    {"id": 106, "name": "USB-C Hub", "category": "Accessories", "price": 2400, "stock": 18, "min_stock": 8},
    {"id": 107, "name": "Wireless Headphones", "category": "Audio", "price": 4500, "stock": 7, "min_stock": 10},
    {"id": 108, "name": "Bluetooth Speaker", "category": "Audio", "price": 2800, "stock": 20, "min_stock": 5},
    {"id": 109, "name": "Laptop Pro 16", "category": "Computers", "price": 95000, "stock": 4, "min_stock": 3},
    {"id": 110, "name": "USB-C Cable", "category": "Accessories", "price": 450, "stock": 50, "min_stock": 20}
]
def display_products(result):
    if len(result) == 0:
        print("No records found")
        return
    for p in result:
        print(p)
 
    print("\nTotal Matching Products :", len(result))
    total_value = 0
    out_of_stock = 0
    lowest = result[0]
    highest = result[0]
 
    for p in result:
        total_value += p["price"] * p["stock"]
 
        if p["stock"] == 0:
            out_of_stock += 1
        if p["price"] < lowest["price"]:
            lowest = p
        if p["price"] > highest["price"]:
            highest = p
 
    print("Total Inventory Value :", total_value)
    print("Out Of Stock Products :", out_of_stock)
    print("Lowest Priced Product :", lowest["name"], lowest["price"])
    print("Highest Priced Product :", highest["name"], highest["price"])
 
 
def multi_field_search():
    term = input("Enter Search Term : ").lower()
    result = []
 
    for p in products:
        if term in p["name"].lower() or term in p["category"].lower():
            result.append(p)
 
    display_products(result)
 
def filtered_search():
    category = input("Category : ").strip()
    try:
        min_price = int(input("Minimum Price : "))
        max_price = int(input("Maximum Price : "))
        min_stock = int(input("Minimum Stock : "))
 
        if min_price < 0 or max_price < 0 or min_stock < 0:
            print("Negative values not allowed")
            return
        if min_price > max_price:
            print("Invalid Price Range")
            return
        stock_choice = input("Only In Stock (y/n) : ").lower()
        result = []
 
        for p in products:
            if category and p["category"].lower() != category.lower():
                continue
            if p["price"] < min_price or p["price"] > max_price:
                continue
            if p["stock"] < min_stock:
                continue
            if stock_choice == "y" and p["stock"] == 0:
                continue
            result.append(p)
        display_products(result)
 
    except ValueError:
        print("Enter Numeric Values Only")
 
def stock_status_search():
    print("1. Out Of Stock")
    print("2. Low Stock")
    print("3. Adequately Stocked")
 
    choice = input("Enter Choice : ")
    result = []
 
    if choice == "1":
        for p in products:
            if p["stock"] == 0:
                result.append(p)
    elif choice == "2":
        for p in products:
            if p["stock"] > 0 and p["stock"] < p["min_stock"]:
                result.append(p)
    elif choice == "3":
        for p in products:
            if p["stock"] >= p["min_stock"]:
                result.append(p)
    else:
        print("Invalid Choice")
        return
 
    display_products(result)
 
def best_match_search():
    term = input("Enter Product Name : ").lower()
    exact = []
    starts = []
    contains = []
 
    for p in products:
        name = p["name"].lower()
        if name == term:
            exact.append(p)
        elif name.startswith(term):
            starts.append(p)
        elif term in name:
            contains.append(p)
    groups = [exact, starts, contains]
 
    for group in groups:
        n = len(group)
        for i in range(n):
            for j in range(n - i - 1):
                if group[j]["price"] > group[j + 1]["price"]:
                    group[j], group[j + 1] = group[j + 1], group[j]
 
    result = exact + starts + contains
    display_products(result)
 
while True:
    print("\n1.Multi Field Search")
    print("2.Filtered Search")
    print("3.Stock Status Search")
    print("4.Best Match Search")
    print("5.Exit")
    choice = input("Enter Choice : ")
 
    if choice == "1":
        multi_field_search()
    elif choice == "2":
        filtered_search()
    elif choice == "3":
        stock_status_search()
    elif choice == "4":
        best_match_search()
    elif choice == "5":
        break
    else:
        print("Invalid Choice")