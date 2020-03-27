import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgres://qoqkcosz:P41XZfuPw6OxY5Y48sBA6o2r6HAcypnc@balarama.db.elephantsql.com:5432/qoqkcosz')
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("books.csv")
    reader = csv.reader(f)
    for isbn, title, author, year in reader:
        if(isbn != 'isbn'):
            db.execute("INSERT INTO libros (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",{"isbn": isbn, "title": title, "author": author, "year": year})
    db.commit()
        
if __name__ == "__main__":
    main()