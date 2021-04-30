# This exercise is the 15th lesson in CodeCademy's Python 2 course
# This isn't horribly complicated, but the intent is to educate rather than to impress.

# prints a list of grades on separate lines
def print_grades(grades_input):
  for grade in grades_input:
    print grade

# sum a list of grades
def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total

# finds the mean of a list of grades
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

# finds the variance of a list of grades
def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  for score in scores:
    variance += ((average - score) ** 2)
  return float(variance) / len(scores)

# finds the standard deviation of a given variance
# CodeCademy used the variance as input, but I reworked this slightly to make inputs consistent
def grades_std_deviation(scores):
  return grades_variance(scores) ** 0.5


# Sample usage

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

print_grades(grades)
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades)
print grades_std_deviation(grades)
