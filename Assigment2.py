# -------------------------------
# LIST (Creation, Modification and Access)
# -------------------------------

print("----- LIST OPERATIONS -----")

# 1. List Creation
age_list = [24, 25, 26, 27, 28]
name_list = ["Arun", "Meena", "Rahul", "Divya", "Kiran"]

print("Initial age_list:", age_list)
print("Initial name_list:", name_list)

# 2. List Operations / Modifications

# a. Append
name_list.append("Yazhini")
print("After appending Yazhini:", name_list)

# b. Insert
age_list.insert(2, 30)
print("After inserting 30 at index 2:", age_list)

# c. Remove
name_list.remove("Yazhini")
print("After removing Yazhini:", name_list)

# d. Pop last element
age_list.pop()
print("After popping last element:", age_list)

# e. Extend
age_list.extend([29, 30, 26])
print("After extending:", age_list)

# f. Sort descending
age_list.sort(reverse=True)
print("After sorting descending:", age_list)

# g. Max, Min and Sum
print("Maximum age:", max(age_list))
print("Minimum age:", min(age_list))
print("Sum of ages:", sum(age_list))


# 3. Accessing List Elements
print("\n----- ACCESSING LIST ELEMENTS -----")

print("First element:", name_list[0])
print("Last element:", name_list[-1])
print("Elements from index 2 to 4:", name_list[2:5])
print("Reverse order:", name_list[::-1])


# -------------------------------
# DICTIONARY (Creation, Modification and Access)
# -------------------------------

print("\n----- DICTIONARY OPERATIONS -----")

# a. Create dictionary
student_marks = {
    "Arun": 75,
    "Meena": 88,
    "Rahul": 92,
    "Divya": 67,
    "Kiran": 81
}

print("Initial dictionary:", student_marks)

# b. Access specific student mark
print("Mark of Rahul:", student_marks["Rahul"])

# c. Add new student
student_marks["Janani"] = 80
print("After adding Janani:", student_marks)

# d. Update mark
student_marks["Arun"] = 82
print("After updating Arun's mark:", student_marks)

# e. keys(), values(), items()
print("All Keys:", student_marks.keys())
print("All Values:", student_marks.values())
print("All Items:", student_marks.items())


# -------------------------------
# SET OPERATIONS
# -------------------------------

print("\n----- SET OPERATIONS -----")

# a. Create set
my_set = {'a','e','i','o','u','a','a','i'}
print("my_set:", my_set)

print("Explanation: Duplicate values are automatically removed in a set.")

# b. Attempt to change value
try:
    my_set[4] = 's'
except Exception as e:
    print("Error:", e)
    print("Explanation: Sets are unordered and do not support indexing.")


# c. Create two sets
set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 8, 10}

# d. Union and Intersection
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))


# -------------------------------
# OPERATORS & CONDITIONAL STATEMENTS
# -------------------------------

print("\n----- PERFORMANCE CATEGORY PROGRAM -----")

score = int(input("Enter your score (0 to 10): "))

if score > 10 or score < 0:
    print("Invalid input! Please enter a score between 0 and 10.")
elif score > 7:
    print("Above Average: Excellent work! Keep it up!")
elif score >= 4:
    print("Average: Good effort! Keep practicing, there's room for improvement.")
else:
    print("Below Average: Need to improve your performance. Consistent practice will lead to better results.")