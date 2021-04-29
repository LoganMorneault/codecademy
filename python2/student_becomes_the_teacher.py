# This project is the 10th lesson of CodeCademy's Python 2 course. It is less guided than the lessons before it but still very easy.
# This project gets remarkably close to traditional Java/C++ classes and structs, which I know will be introduced here later on.
# Very little is changed between this implementation and the one I submitted online.

# Students are represented as a dictionary with a name and lists for their homework, quiz, and test scores.
# Three students are manually created here.
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

# averages a list of 3 numbers 
def average(numbers):
  total = float(sum(numbers))
  return total / len(numbers)

# find the student's grade
def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  return homework * .1 + quizzes * .3 + tests * .6

# converts a numeric grade to a letter grade
def get_letter_grade(score):
  if score >= 90:
    return "A"
  if score >= 80:
    return "B"
  if score >= 70:
    return "C"
  if score >= 60:
    return "D"
  else:
    return "F"

# gets the average grade of a list of students
def get_class_average(class_list):
  results = []
  for student in class_list:
    results.append(get_average(student))

  return average(results)


# Sample usage

students = [alice, lloyd, tyler]
class_average = get_class_average(students)
print class_average
print get_letter_grade(class_average)
