import math

def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  return num1 / num2

def cos(num):
  return math.cos(num)

def inverseCos(num):
  return math.acos(num)

def sin(num):
  return math.sin(num)

def inverseSin(num):
  return math.asin(num)

def tan(num):
  return math.tan(num)

def inverseTan(num):
  return math.atan(num)

def square(num, power):
  if power is not 2:
    return "The should be 2!"
  else:
    return math.pow(num, power)

def cube(num, power):
  if power is not 3:
    return "The power should be 3!"
  else:
    return math.pow(num, power)
