
class LibraryItem:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Book(LibraryItem):
    def __init__(self, title, author, price, category, available):
        super().__init__(title, author)
        self.price = price
        self.category = category
        self.available = available

    def display(self):
        print(
            f"Title: {self.title}, "
            f"Author: {self.author}, "
            f"Price: ₹{self.price:.2f}, "
            f"Category: {self.category}, "
            f"Available: {self.available}"
        )


books = []
invalid_lines = []

# Read books from books.txt
try:
    with open("books.txt", "r") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()

            if not line:
                continue

            try:
                fields = line.split(",")

                # Validate the number of fields
                if len(fields) != 5:
                    raise ValueError("Missing or extra fields")

                title = fields[0].strip()
                author = fields[1].strip()
                price_text = fields[2].strip()
                category = fields[3].strip()
                available_text = fields[4].strip().lower()

                # Validate missing fields
                if not title or not author or not category or not price_text:
                    raise ValueError("Required field is missing")

                # Validate price
                price = float(price_text)

                if price < 0:
                    raise ValueError("Price cannot be negative")

                # Validate availability
                if available_text not in ("true", "false"):
                    raise ValueError(
                        "Available must be True or False"
                    )

                available = available_text == "true"

                # Create Book object
                book = Book(
                    title, author, price, category, available
                )

                books.append(book)

            except ValueError as error:
                invalid_lines.append(
                    f"Line {line_number}: {line} - {error}"
                )

except FileNotFoundError:
    print("Error: books.txt file not found.")

# Display invalid records
if invalid_lines:
    print("\nInvalid records:")
    for record in invalid_lines:
        print(record)

# Check whether books were loaded
if books:

    # Sort books by price without built-in sorting
    for i in range(len(books)):
        for j in range(0, len(books) - i - 1):
            if books[j].price > books[j + 1].price:
                temp = books[j]
                books[j] = books[j + 1]
                books[j + 1] = temp

    # Display sorted books
    print("\n--- BOOKS SORTED BY PRICE ---")
    for book in books:
        book.display()

    # Group books by category
    print("\n--- BOOKS GROUPED BY CATEGORY ---")

    categories = []

    for book in books:
        if book.category not in categories:
            categories.append(book.category)

    for category in categories:
        print(f"\nCategory: {category}")

        for book in books:
            if book.category == category:
                book.display()

    # Display books costing less than ₹500
    print("\n--- BOOKS COSTING LESS THAN ₹500 ---")

    found = False

    for book in books:
        if book.price < 500:
            book.display()
            found = True

    if not found:
        print("No books found below ₹500.")

    # Count available and unavailable books
    available_count = 0
    unavailable_count = 0

    for book in books:
        if book.available:
            available_count += 1
        else:
            unavailable_count += 1

    print("\n--- AVAILABILITY COUNT ---")
    print("Available books:", available_count)
    print("Unavailable books:", unavailable_count)

    # Calculate average book price
    total_price = 0

    for book in books:
        total_price += book.price

    average_price = total_price / len(books)

    print(f"\nAverage book price: ₹{average_price:.2f}")

    # Save sorted books to sorted_books.txt
    with open("sorted_books.txt", "w") as file:
        file.write("title,author,price,category,available\n")

        for book in books:
            file.write(
                f"{book.title},{book.author},"
                f"{book.price:.2f},{book.category},"
                f"{book.available}\n"
            )

    print("\nSorted books saved to sorted_books.txt")

else:
    print("\nNo valid books available to process.")
