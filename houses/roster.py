from sys import argv
from cs50 import SQL
import csv

def main():
    if len(argv) == 2:
        db = SQL("sqlite:///students.db")
        all_rows = db.execute("SELECT DISTINCT first, middle, last, birth FROM students WHERE house = ? ORDER BY last, first", argv[1])
        
        for row in all_rows:
            if row["middle"] != None:
                middle = row["middle"].strip()
                print(row["first"] + " " + row["middle"] + " " + row["last"] + ",born " + str(row["birth"]))
            else:
                print(row["first"] + " " + row["last"] + ", born" + str(row["birth"]))
        
    else:
        print("Usage: python roster.py house-name")
        exit(1)
    

main()