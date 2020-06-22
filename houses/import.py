import csv
from sys import argv, exit
from cs50 import SQL

def main():
    if len(argv) != 2:
        print("Usage: python import.py file.csv")
        exit(1)

    csv_path = argv[1]

    if not (csv_path.endswith(".csv")):
        print("You must provide a .csv file")
        exit(1)
    
    open("students.db", "w").close()
    db = SQL("sqlite:///students.db")
    
    db.execute("CREATE TABLE students (first TEXT, middle TEXT, last TEXT, house TEXT, birth NUMERIC)")

    with open(csv_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            array = []
            array.append(row["name"].split())
            name = array[0]
            if len(name) == 2:
                db.execute("INSERT INTO students(first, middle, last, house, birth) VALUES (?,?,?,?, ?)", name[0], None, name[1], row["house"], int(row["birth"]))
            if len(name) == 3:
                db.execute("INSERT INTO students(first, middle, last, house, birth) VALUES (?,?,?,?,?)", name[0], name[1], name[2], row["house"], int(row["birth"]))


main()