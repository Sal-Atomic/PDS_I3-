#1. Student Profile Card
name = "Sok Dara"
age = 20
major = "Data Science"
gpa = 4.0
scholar = True

print("=" * 30)
print(f"Name    : {name}")
print(f"Age     : {age}")
print(f"Major   : {major}")
print(f"GPA     : {gpa:.2f}")
print(f"Scholar : {scholar}")
print("=" * 30)
for n in [name, age, major, gpa, scholar]:
  print(n, type(n), sep=" -> ")
