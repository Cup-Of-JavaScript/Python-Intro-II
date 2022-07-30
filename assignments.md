# Python Intro II Assignments
Submit a PR for each exercise.

# Ex. 1 Sort with Lambda
Given the following list:

```
people_list = [
    {'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1},
    {'name': 'bob', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
]
```

Create a function called `sort_people()` that accepts the following arguments:
  - A list of people
  - A field that will used to sort the people (e.g. name, age, weight, etc...)
  - The sort direction (e.g. asc or desc)

This function must use a Lambda function to perform the sort.

The function is used in the following manner:

```
def ex1():
    people_list = [
        {'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1},
        {'name': 'bob', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    sort_people(people_list, 'weight', 'desc')
    print(people_list)
```

Output:
```
[{'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1}, {'name': 'bob', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2}, {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3}]
```

# Ex. 2 Filter
Given the following list:

```
people_list = [
    {'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1},
    {'name': 'bob', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
]
```

Create a function called `filter_males()` that accepts the following arguments:
    - A list of people

This function returns only the males from the list of people.

The function is used in the following manner:

```
def ex2():
    people_list = [
        {'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1},
        {'name': 'bob', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    filtered_list = filter_males(people_list)
    print(filtered_list)
```
Output:
```
[{'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1}, {'name': 'bob', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2}]
```

# Ex. 3 Map


BMI = kg/m<sup>2</sup>


# Ex. 4 List Comprehension

# Ex. 5 SQS

# Ex. 6 Postgres DB

# Ex. 7 AWS S3

# Ex. 8 Requests
