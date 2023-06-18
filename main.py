person = {
    "name": "John Doe",
    "age": 30,
    "gender": "male"
}

print(person["name"])
print(person["age"])

book = {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925
}

print(book["The Great Gatsby"], book["F. Scott Fitzgerald"], book["1925"])

student = {
    "name": "John Doe",
    "grade1": 80,
    "grade2": 90
}

student["average"] = (student["grade1"] + student["grade2"]) / 2

print(student)
{'name': 'John Doe', 'grade1': 80, 'grade2': 90, 'average': 85}

def sum(a, b):
    return a + b