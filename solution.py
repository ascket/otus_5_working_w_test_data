import json, csv
from files import JSON_FILE_PATH
from files import CSV_FILE_PATH
from files import get_path

users_with_books = []

with open(JSON_FILE_PATH) as file:
    users = json.loads(file.read())

with open(CSV_FILE_PATH) as file:
    books = csv.reader(file)
    header = next(books)
    for x in range(len(users)):
        users_with_books.append({
            "name": users[x]["name"],
            "gender": users[x]["gender"],
            "address": users[x]["address"],
            "age": users[x]["age"],
            "books": []
        })
    while True:
        try:
            for x in range(len(users_with_books)):
                book = next(books)
                users_with_books[x]["books"].append({
                    "title": book[0],
                    "author": book[1],
                    "pages": book[3],
                    "genre": book[2]
                })
        except StopIteration:
            break

with open(get_path("result.json"), "w") as file:
    strg = json.dumps(users_with_books, indent=4)
    file.write(strg)
