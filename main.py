student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

grade_book = {}
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        grade_book[student] = 'Outstanding!'
    elif score > 80:
        grade_book[student] = 'Exceeds Expectations'
    elif score > 70:
        grade_book[student] = 'Acceptable'
    else:
        grade_book[student] = 'Fail'

print(grade_book)
