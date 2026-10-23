#2. Time Converter
total_seconds = 9875
hours = total_seconds//3600
minutes = (total_seconds%3600)//60
seconds = ((total_seconds%3600)%60)
print(f"{hours} hours {minutes} minutes {seconds} seconds")
