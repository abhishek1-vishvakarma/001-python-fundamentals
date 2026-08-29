# Json In python

# JSON (JavaScript Object Notation) is a lightweight format used to store and exchange data.


# As an AI/Backend Engineer, JSON is very important because APIs, FastAPI, databases, configuration files, and AI applications use JSON heavily.

# 1. What does JSON look like?
# Example:
# {
#     "name": "Abhishek",
#     "age": 23,
#     "skills": ["Python", "FastAPI", "AI"],
#     "is_active": true,
# }

# JSON  -> Python
# Object -> Dictionary dict
# Array [] -> List list
# String -> str
# Number -> int/float
# true -> True
# false -> False
# null -> None


# 2. Python json Module

import json

# four important functions

# json.dumps() -> python -> JSON string
# json.loads() -> JSON string -> Python

# json.dump() -> Python -> JSON file
# json.load() -> JSON file -> python


# 3. Python Dictionary → JSON String
# user = {
#   "name": "Abhishek",
#   "age": 25,
#   "role": "AI Engineer"
# }

# json_data = json.dumps(user)

# print(json_data)

# Pretty JSON

# json_data = json.dumps(user, indent=4)
# print(json_data1)


# 4. JSON String → Python Dictionary

# json_data = '{"name": "Abhishek", "age": 23}'
# user = json.loads(json_data)

# print(user)
# print(user["name"])
# print(user.get("name")) #get() method

# 5. Write JSON to a File ⭐

# user = {
#   "name": "Abhishek",
#   "age": 25,
#   "role": "AI Engineer"
# }

# with open("user.json", "w") as file:
#   json.dump(user, file, indent=4)

# 6. Read JSON from a File ⭐
# user = {
#   "name": "Abhishek",
#   "age": 25,
#   "role": "AI Engineer"
#   }

# with open("user.json", 'r') as file:
#   user = json.load(file)

#   print(user)
#   print(user["name"])

# 7. dump() vs dumps()

# This is very important.

# dumps()

# s = string
# Python → JSON string
# json_string = json.dumps(user)
# dump()
# Python → JSON file
# json.dump(user, file)

# Remember:
# dumps → String
# dump  → File

# 8. load() vs loads()

# loads()

# s = string
# JSON string → Python
# user = json.loads(json_string)

# load()

# JSON file → Python

# user = json.load(file)

# Remember:

# loads → String
# load  → File

# 9 complete example:

# user = {
#   "name": "Abhishek",
#   "age": 25,
#   "skills": [
#     "Python",
#     "FastAPI",
#     "Machine Learning"
#   ],
#   "is_active": True
# }

# python -> JSON String

# json_data = json.dumps(user, indent=4)
# print(json_data)


# JSON String -> Python

# json_data = json.loads(json_data)
# print(json_data)
# print(json_data["name"])
# print(json_data["skills"])


# # Python → JSON File
# with open("user.json", "w") as file:
#     json.dump(user, file, indent=4)


# JSON File → Python
# with open("user.json", "r") as file:
#     data = json.load(file)

# print(data)

# 10. JSON with Exception Handling

# Very useful in real applications:

try:
  with open("user.json", "r") as file:
    data = json.load(file)

  print(data)
except FileNotFoundError:
  print("JSON file not found")

except json.JSONDecodeError:
  print("Invalid JSON format")

#11. JSON in APIs ⭐⭐⭐
# This is very important for your AI Engineer path.

# Suppose a frontend sends:
# {
#     "question": "What is the leave policy?"
# }

from pydentic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Question(BaseModel):
     question: str

@app.post("/ask")
def ask_question(data: Question):
   return {
      "answer": f"You asked: {data.question}"
   }

#Request:
{
   "question": "What is the leave policy?"
}

#Response:

{
    "answer": "You asked: What is the leave policy?"
}

# ⭐ What You Should Remember
#                 JSON
#                   │
#           ┌───────┴────────┐
#           │                │
#        String             File
#           │                │
#      ┌────┴────┐      ┌────┴────┐
#      │         │      │         │
#  dumps()    loads()  dump()    load()
#      │         │      │         │
#  Python →   JSON →   Python →  JSON →
#  JSON       Python   File      Python

