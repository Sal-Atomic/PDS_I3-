#Temperature Converter
def celsius_to_fahrenheit(c, round_to=1):
  F = (c*9/5+32)
  return(F, round_to)
def fahrenheit_to_celsius(f, round_to=1):
  C = (f - 32)*5/9
  return(c, round_to)

#(a) Use a for loop with range(0, 101, 20) to print the conversion table below
for c in range (0, 101, 20):
  celsius_to_fahrenheit(c, round_to=1)