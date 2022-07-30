# Python Intro II Assignments
Submit a PR for each exercise.

Use this [Python Reference](https://gitlab.com/mburolla/python-reference/) as a guide to these exercises.

# Ex. 1 Sort with Lambda
Given the following list:

```python
people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
]
```

Create a function called `sort_people()` that accepts the following arguments:
  - A list of people
  - A field that will used to sort the people (e.g. name, age, weight, etc...)
  - The sort direction (e.g. asc or desc)

This function must use a Lambda function to perform the sort.

Usage:

```python
def ex1():
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    sort_people(people_list, 'weight', 'desc')
    print(people_list)
```

Output:
```
[{'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1},
 {'name': 'bob', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2}, 
 {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3}]
```

# Ex. 2 Filter
Given the following list:

```python
people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
]
```

Create a function called `filter_males()` that accepts the following arguments:
- A list of people

This function returns only the males from the list of people.

The function is used in the following manner:

```python
def ex2():
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    filtered_list = filter_males(people_list)
    print(filtered_list)
```
Output:
```
[{'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1}, 
{'name': 'bob', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2}]
```

# Ex. 3 Map
Given the following list:

```python
people_list = [
    {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
    {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
]
```

Create a function called `calc_bmi()` that accepts this list and calculates the BMI (Body Mass Index) for 
each person.  The formula for BMI is:  BMI = weight/height<sup>2</sup>.  This can be expressed in python
using this syntax: `round(weight / height ** 2, 1)`.

The `calc_bmi()` function must use the `map()` function.

Usage:
```python
def ex3():
    people_list = [
        {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
        {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
    ]
    new_people_list = calc_bmi(people_list)
    print(new_people_list)
```

Output:
```
[{'id': 2, 'name': 'bob', 'weight_kg': 90, 'height_meters': 1.7, 'bmi': 31.1}, 
{'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8, 'bmi': 24.7}]
```

# Ex. 4 List Comprehension
Given the following list:

```python
people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
]
```

Create a function called `get_people()` that accepts a list of people.  Use a list comprehension
to return the names of people that are equal to or greater than 15 years old.

Usage:
```python
def ex4():
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    print(get_people(people_list))
```

Output:
```
['alice', 'charlie']
```

# Ex. 5 SQS
Create the following functions:
  - send_message_to_sqs()
  - read_message_from_sqs()

The `send_message_to_sqs()` function sends a cat to SQS and `read_message_from_sqs()` reads a message from SQS.

**NOTE**: Be sure to use the SQS queue that corresponds with your student id!

`https://sqs.us-east-1.amazonaws.com/807758713182/stu-{student id}`

Usage:
```python
def ex5():
    cat = {
        "cat_id": 1,
        "cat_name": "Gypsy",
        "status": "hungry"
    }
    response = send_message_to_sqs(cat, 'https://sqs.us-east-1.amazonaws.com/807758713182/stu-0')
    while True:
        time.sleep(3)
    msg = read_message_from_sqs('https://sqs.us-east-1.amazonaws.com/807758713182/stu-0')
        if msg:
            print(msg)
        else:
            now = datetime.now().strftime("%H:%M:%S")
            print(f"Polling SQS { now }...")
```

Output:
```
{'status': 'hungry', 'cat_id': '1', 'cat_name': 'Gypsy'}
Polling SQS 16:34:30...
Polling SQS 16:34:33...
Polling SQS 16:34:36...
```

# Ex. 6 Postgres Insert Cat
Create a new database on your local Postgres instance called Cats.  Create a cat table with the 
following schema:

```
cat_id: Integer
cat_name: Text
status: Text
```
Create a function called `save_to_cat_table()` that accepts a Cat object and saves it to the table.

Usage:
```python
def ex6():
    cat = {
        "cat_id": 1,
        "cat_name": "Gypsy",
        "status": "hungry"
    }
    save_to_cat_table(cat)
```

Output:
Nothing on the terminal, check the database table (`select * from cat`)

# Ex. 7 Postgres Get Cat
Create a function called `get_cat()` that accepts an integer which returns the cat for the id passed
into this function.

Usage:
```python
def ex7():
    cat_id = 1
    cat = get_cat(cat_id)
    print(cat)
```

Output:
```
(1, 'gypsy', 'hungry')
```

Hint: Cast the cat_id to a string inside the `get_cat()` function.  Also, use `fetchone()`.
