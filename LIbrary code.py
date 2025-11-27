import csv

FILE_NAME = "library.csv"

def create_file():
    try:
        with open(FILE_NAME, "x", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Book Name", "Author", "Status"])
    except FileExistsError:
        pass

def add_book():
    name = input("Enter book name: ")
    author = input("Enter author: ")

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, author, "Available"])

    print("Book added successfully!")

def view_books():
    print("\nAvailable Books:\n")
    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        next(reader)

        for name, author, status in reader:
            if status == "Available":
                print(f"{name} — {author}")

def issue_book():
    book_name = input("Enter book name to issue: ")
    updated = []

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[0] == book_name and row[2] == "Available":
                row[2] = "Issued"
            updated.append(row)

    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Book Name", "Author", "Status"])
        writer.writerows(updated)

    print("Book issued successfully!")

def return_book():
    book_name = input("Enter book name to return: ")
    updated = []

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[0] == book_name and row[2] == "Issued":
                row[2] = "Available"
            updated.append(row)

    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Book Name", "Author", "Status"])
        writer.writerows(updated)

    print("Book returned successfully!")

def show_menu():
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

create_file()

while True:
    show_menu()
    choice = input("Choose option: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice! Try again.")
