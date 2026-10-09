import numpy as np

student_scores = np.array([
    [85, 90, 78, 88],
    [75, 80, 85, 70],
    [90, 95, 88, 92],
    [80, 85, 90, 82]
])

subjects = ["Math", "Science", "English", "History"]

averages = np.mean(student_scores, axis=0)

print("AVERAGE MARKS OF EACH SUBJECT")

for i in range(4):
    print(subjects[i], ":", averages[i])

max_index = np.argmax(averages)

print("Subject with highest average:", subjects[max_index])
print("Highest average:", averages[max_index])
