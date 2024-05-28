# Lab17 - Practice for the final exam

<a href= "http://xkcd.com/844/" alt = "Good code comic xkcd"><img src="http://www.the-chaos.com/alvin/cs149spring2023/labs/lab-22-review/good_code.png" alt = "Good code comic xkcd"></a>

The final exam consists of two parts (written and coding). Each part will be worth 50 points.

Instructions
Here is some practice for the final exam.  Answer keys will not be provided(you should be able to plug these into Thonny to find answers mostly).  You may ask for clarifications or answers for specific questions though.
A written exam based on one used in 2022, this is not exact content that will be on the final exam, but rather some concepts to study.

This is a practice problem only for timing purposes and may not reflect content coverage on the actual final.  The final will likely have more coding questions
than just these two.

Submit via Gradescope for the coding portion.
Let me know if you have any questions, and good luck!
-------------------------------------------------------------------------
## Written Exam Practice

## 1. Circle and label an example of each of the following in the code sample below.
    A. local variable
    B. global variable
    C. method call
    D. dictionary
    E. list
    F. relational operator
    G. assignment operator
    H. Boolean operator
    I. method definition
    J. parameter
    K. argument

```
import sys
MIN_CHARGE = 10.0

global total_fees

def add_student(students, name, sid):
# students is a list of dictionaries of student
    new_stu = {
        "name": name,
        "id": sid,
        "balance": 0
    }
    students.append(new_stu)

def apply_charge(students, sid, amount):
    global total_fees
    charge = amount
    charged = False
    if charge <= MIN_CHARGE:
        charge = MIN_CHARGE
    for student in students:
        if student["id"] == sid:
            student["balance"] += charge
            total_fees += charge
            charged = True
    return charged

if __name__ == "__main__":
    roster = []
    total_fees = 0.0
    john = add_student(roster, "John", 1000)
    alice = add_student(roster, "Alice", 1001)
    apply_charge(roster, 1001, 0)
    print(total_fees)
```


## 2. Tracing Code
Determine what will be printed by each of the following code snippets given the code from the previous page. Each snippet should be considered independently: do not assume that they are executed sequentially, or that the code in the __name__ == “__main__” block has been executed. If a snippet will result in an error, write ERROR.

### A.
```
    stu_a = []
    add_student(stu_a, "Greta", 1000)
    apply_charge(stu_a, 1000, 5.0)
    print(total_fees)
```
### B.
```
    stu_b = []
    add_student(stu_b, "Greta", 1000)
    add_student(stu_b, "Harry", 1001)
    apply_charge(stu_b, 1000, 12.0)
    apply_charge(stu_b, 1001, 6.0)
    print(f"{stu_b[0].get('balance')}")
    print(f"{stu_b[1].get('balance')}")
    print(total_fees)
```
### C.
```
    stu_c = []
    add_student(stu_c, "Greta", 1000)
    add_student(stu_c, "Harry", 1001)
    add_student(stu_c, "Harry", 1002)
    apply_charge(stu_c, 1002, 12.0)
    apply_charge(stu_c, 1001, 6.0)
    print(f"{stu_c[0].get('balance')}")
    print(f"{stu_c[1].get('balance')}")
    print(f"{stu_c[2].get('balance')}")
```
### D.
```
    stu_d = []
    add_student(stu_d, "Greta", 1000)
    add_student(stu_d, "Greta", 1000)
    apply_charge(stu_d, 1000, 100.0)
    print(stu_d[0] is stu_d[1])
    print(stu_d[0] == stu_d[1])
```
### E.
```
    stu_e = []
    add_student(stu_e, "Greta", 1000)
    print(stu_e[0] == "Greta")
```


## 3. Nested For Loops
Determine what will be printed by each of the code snippets below.

a.
```
letters = [["A", "B", "C"], ["X", "Y"]]
result = ""
for var1 in letters:
    for var2 in var1:
        result += var2
    result += "\n"
print(result)

```





b.
```
var1 = "cat bat"
var2 = var1.split()
for first in var2:
    print(first)
    for second in first:
        print(second)
```




c.
```
result = ""
for i in range(2, 5):
    for j in range(i):
        result += "*"
    result += "\n"
print(result)
```





## 4. Finding Errors
For each set of code snippets below, only one of the options will execute without error. Circle the block that will execute successfully.

a.
```
my_dictionary = { "a": 1, "b": 2, "c": 3 }
for i in range(0, len(my_dictionary)):
      print(my_dictionary[i])
```
or
```
my_dictionary = { "a": 1, "b": 2, "c": 3 }
for i in my_dictionary:
print(f"{i} -> { my_dictionary[i] }")
```

b.
```
my_dictionary = { "a": 1, "b": 2, "c": 3 }
while i in my_dictionary:
      print(f"{i} -> { my_dictionary[i] }")
      i += 1
```
or
```
my_dictionary = { "a": 1, "b": 2, "c": 3 }
for i in my_dictionary:
      print(i + " -> " + str(my_dictionary[i]))
```

c.
```
my_dictionary = { "a": 1, "b": 2, "c": 3 }
if len(my_dictionary) > 7:
      print("this is a large dictionary.")
else:
      print("this is a normal-sized dictionary.")
elif len(my_dictionary) < 3:
      print("this is a small dictionary.")
```
or
```
my_dictionary = { "a": 1, "b": 2, "c": 3 }
if len(my_dictionary) > 7:
      print("this is a large dictionary.")
elif 3 <= len(my_dictionary) <= 7:
      print("this is a normal-sized dictionary.")
else:
      print("this is a small dictionary.")
```
or
```
my_dictionary = { "a": 1, "b": 2, "c": 3 }
      if len(my_dictionary) > 7:
      print("this is a large dictionary.")
elif 3 < len(my_dictionary) < 7:
      print("this is a normal-sized dictionary.")
else:
      print("this is a small dictionary.")
```

## 5. File I/O

<pre>
def add_numbers_in_file(file_name):
    """Return the sum of all numbers that appear in the provided file.
    Each line in the file will contain an arbitrary sequence
    of numbers separated by white-space. This function will read
    the file and return the sum of all numbers. For example, if the file
    contains the following four lines:
    12.0 2.0
    6.0
    10.0 2.5 2.5
    Then the return value will be 35.0
    Args:
        file_name (str): The name of a file. E.g. "numbers.txt"
    Returns:
        float: The sum of all numbers stored in the indicated file.
    """
</pre>

-------------------------------------------------------------------------

Coding Problem:

```
"""scheduler - a course schedule planner.

@author: YOUR NAME
@version: DUE DATE
"""

def plan_workload(schedule):
    """Plan course workload for semester given the list of courses.
    The schedule is a list of courses(which is a dict containing 3 elements:
    a) string prefix(ie. CS for Computer Science
    b) int number like 149 for CS149
    c int credits = # of credit hours for the course

    Args:
        schedule(list): a list of courses as described above

    Returns:
        (int): The workload for a set of courses is measured in points.
        Lower division courses (with numbers below 300) get two points,
        upper division courses (in the 300-499 range) get three points,
        and graduate courses (500 and above) get four points.
        CS and MATH courses get an extra point.
        3 credit or lower courses get 1 point while 4 credit courses get 2 and 5 credit ones receive 3 points. If the schedule has zero courses or equals None, then plan_workload should return -1
    """
    pass

def find_hardest(schedule):
    """Find hardest course for a scheduled list of courses.
    The schedule is a list of courses(which is a dict containing 3 elements:
    a) string prefix(ie. CS for Computer Science b)int number like 149 for CS149
    c) int credits = # of credit hours for the course

    Args:
        schedule(list): a list of courses as described above

    Returns:
        (str): Name of last in the list most difficult course(ie most points, CS149 note no space between prefix and number).
        If the schedule has zero courses or equals None, then find_hardest should return "Invalid").
    """
    pass


if __name__ == "__main__":
    my_sched = []
    course1 = {
        "prefix": "CS",
        "number": 169,
        "credits": 3
    }
    course2 = {
        "prefix": "CS",
        "number": 240,
        "credits": 3
    }
    course3 = {
        "prefix": "HIST",
        "number": 101,
        "credits": 3
    }
    my_sched.append(course1)
    my_sched.append(course2)
    my_sched.append(course3)
```
