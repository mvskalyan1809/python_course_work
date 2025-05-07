def star_pattern():
  return '''
  ***Star Pattern***

  n = int(input("Enter number of rows: "))
  for i in range(1, n+1):
    print("*" * i)
  ==========================================
  Testcase-1:
  Enter number of rows: 5
  Output:
  *
  **
  ***
  ****
  *****
  ===========================================
  '''
def diamond_pattern():
  return '''
  ***Diamond Pattern***

  n = int(input("Enter number of rows: "))
  for i in range(n):
    print(" "*(n-i-1) + "*"*(2*i+1))
  for i in range(n-2, -1, -1):
    print(" "*(n-i-1) + "*"*(2*i+1))
  ==========================================
  Testcase-1:
  Enter number of rows: 3
  Output:
    *
   ***
  *****
   ***
    *
  ===========================================
  '''
def kms_to_miles():
  return '''
  ***Kilometers to Miles***

  km = float(input("Enter distance in kilometers: "))
  miles = km * 0.621371
  print("Distance in miles:", miles)
  ==========================================
  Testcase-1:
  Enter distance in kilometers: 10
  Output:
  Distance in miles: 6.21371
  ===========================================
  '''
def miles_to_kms():
  return '''
  ***Miles to Kilometers***

  miles = float(input("Enter distance in miles: "))
  km = miles / 0.621371
  print("Distance in kilometers:", km)
  ==========================================
  Testcase-1:
  Enter distance in miles: 6.21371
  Output:
  Distance in kilometers: 10.0
  ===========================================
  '''
def cms_to_inches():
  return '''
  ***Centimeters to Inches***

  cm = float(input("Enter length in centimeters: "))
  inches = cm / 2.54
  print("Length in inches:", inches)
  ==========================================
  Testcase-1:
  Enter length in centimeters: 10
  Output:
  Length in inches: 3.937007874015748
  ===========================================
  '''
def degrees_to_radians():
  return '''
  ***Degrees to Radians***

  import math
  degrees = float(input("Enter angle in degrees: "))
  radians = degrees * (math.pi / 180)
  print("Angle in radians:", radians)
  ==========================================
  Testcase-1:
  Enter angle in degrees: 180
  Output:
  Angle in radians: 3.141592653589793
  ===========================================
  '''
def distance_between_points():
  return '''
  ***Distance Between Two Points***

  import math
  x1 = float(input("Enter x1: "))
  y1 = float(input("Enter y1: "))
  x2 = float(input("Enter x2: "))
  y2 = float(input("Enter y2: "))
  distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
  print("Distance:", distance)
  ==========================================
  Testcase-1:
  x1: 0, y1: 0, x2: 3, y2: 4
  Output:
  Distance: 5.0
  ===========================================
  '''
def multiplication_table():
  return '''
  ***Multiplication Table***

  n = int(input("Enter number: "))
  for i in range(1, 11):
    print(n, "x", i, "=", n*i)
  ==========================================
  Testcase-1:
  Enter number: 5
  Output:
  5 x 1 = 5
  ...
  5 x 10 = 50
  ===========================================
  '''
def percentage_of_5_subjects():
  return '''
  ***Percentage of 5 Subjects***

  total = 0
  for i in range(5):
    mark = float(input("Enter mark for subject " + str(i+1) + ": "))
    total += mark
  percentage = (total / 500) * 100
  print("Percentage:", percentage)
  ==========================================
  Testcase-1:
  Marks: 80, 70, 90, 85, 75
  Output:
  Percentage: 80.0
  ===========================================
  '''
def power_of_number():
  return '''
  ***Power of a Number***

  base = float(input("Enter base: "))
  exponent = int(input("Enter exponent: "))
  result = 1
  for i in range(abs(exponent)):
    result *= base
  if exponent < 0:
    result = 1 / result
  print("Result:", result)
  ==========================================
  Testcase-1:
  base: 2, exponent: 3
  Output:
  Result: 8
  ===========================================
  '''
def alphabetic_order():
  return '''
  ***Alphabetic Order***

  s = input("Enter a string: ")
  words = s.split()
  words.sort()
  print("Sorted words:")
  for word in words:
    print(word)
  ==========================================
  Testcase-1:
  Input: "banana apple cherry"
  Output:
  apple
  banana
  cherry
  ===========================================
  '''
def student_grade_calculation():
  return '''
  ***student grade calculation***

  marks = int(input("Enter marks (0-100): "))
  if marks >= 90:
    grade = 'A'
  elif marks >= 80:
    grade = 'B'
  elif marks >= 70:
    grade = 'C'
  elif marks >= 60:
    grade = 'D'
  else:
    grade = 'F'
  print("Grade:", grade)

  ==========================================
  Testcase-1:
  Enter marks (0-100): 85
  output:
  Grade: B
  ------------------------------------------
  Testcase-2:
  Enter marks (0-100): 45
  output:
  Grade: F
  ===========================================
  '''
def capitalize_alternate_word():
  return '''
  ***capitalize alternate word***

  sentence = input("Enter a sentence: ")
  words = sentence.split()
  for i in range(len(words)):
    if i % 2 == 0:
      words[i] = words[i].capitalize()
  result = ' '.join(words)
  print(result)

  ==========================================
  Testcase-1:
  Enter a sentence: hello world this is python
  output:
  Hello world This is Python
  ------------------------------------------
  Testcase-2:
  Enter a sentence: alternate capital words
  output:
  Alternate capital Words
  ===========================================
  '''
def fibonacci_series_recursion():
  return '''
  ***fibonacci series using recursion***

  def fib(n):
    if n <= 1:
      return n
    else:
      return fib(n-1) + fib(n-2)

  terms = int(input("Enter number of terms: "))
  for i in range(terms):
    print(fib(i), end=' ')

  ==========================================
  Testcase-1:
  Enter number of terms: 5
  output:
  0 1 1 2 3
  ------------------------------------------
  Testcase-2:
  Enter number of terms: 7
  output:
  0 1 1 2 3 5 8
  ===========================================
  '''
def strong_password_validator():
  return '''
  ***strong password validator***

  pwd = input("Enter password: ")
  if (len(pwd) >= 8 and
      any(c.isupper() for c in pwd) and
      any(c.islower() for c in pwd) and
      any(c.isdigit() for c in pwd) and
      any(c in "!@#$%^&*()" for c in pwd)):
    print("Strong password")
  else:
    print("Weak password")

  ==========================================
  Testcase-1:
  Enter password: Pass123!
  output:
  Strong password
  ------------------------------------------
  Testcase-2:
  Enter password: pass
  output:
  Weak password
  ===========================================
  '''
def count_and_replace_vowels():
  return '''
  ***count and replace vowels in a sentence***

  sentence = input("Enter a sentence: ")
  count = 0
  new_sentence = ''
  for ch in sentence:
    if ch.lower() in 'aeiou':
      count += 1
      new_sentence += '*'
    else:
      new_sentence += ch
  print("Vowels count:", count)
  print("Modified sentence:", new_sentence)

  ==========================================
  Testcase-1:
  Enter a sentence: hello world
  output:
  Vowels count: 3
  Modified sentence: h*ll* w*rld
  ------------------------------------------
  Testcase-2:
  Enter a sentence: AI is fun
  output:
  Vowels count: 4
  Modified sentence: ** *s f*n
  ===========================================
  '''
def custom_math_module():
  return '''
  ***custom math module***

  print("1. Add  2. Subtract  3. Multiply  4. Divide")
  choice = int(input("Choose operation (1-4): "))
  a = int(input("Enter first number: "))
  b = int(input("Enter second number: "))

  if choice == 1:
    print("Result:", a + b)
  elif choice == 2:
    print("Result:", a - b)
  elif choice == 3:
    print("Result:", a * b)
  elif choice == 4:
    if b != 0:
      print("Result:", a / b)
    else:
      print("Cannot divide by zero")
  else:
    print("Invalid choice")

  ==========================================
  Testcase-1:
  Choose operation (1-4): 1
  Enter first number: 5
  Enter second number: 3
  output:
  Result: 8
  ------------------------------------------
  Testcase-2:
  Choose operation (1-4): 4
  Enter first number: 10
  Enter second number: 0
  output:
  Cannot divide by zero
  ===========================================
  '''
def word_length_filter():
  return '''
  ***word length filter***

  sentence = input("Enter sentence: ")
  length = int(input("Enter word length to filter: "))
  words = sentence.split()
  result = [w for w in words if len(w) >= length]
  print("Filtered words:", result)

  ==========================================
  Testcase-1:
  Enter sentence: this is a simple test
  Enter word length to filter: 4
  output:
  Filtered words: ['this', 'simple', 'test']
  ------------------------------------------
  Testcase-2:
  Enter sentence: python is fun
  Enter word length to filter: 3
  output:
  Filtered words: ['python', 'fun']
  ===========================================
  '''
def count_digit_frequency():
  return '''
  ***count digit frequency***

  number = input("Enter a number: ")
  for d in '0123456789':
    count = number.count(d)
    if count > 0:
      print(f"{d}: {count}")

  ==========================================
  Testcase-1:
  Enter a number: 112233
  output:
  1: 2
  2: 2
  3: 2
  ------------------------------------------
  Testcase-2:
  Enter a number: 900009
  output:
  0: 4
  9: 2
  ===========================================
  '''
