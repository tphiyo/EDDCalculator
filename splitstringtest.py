lmp = input("Please enter your last menstrual cycle date in the format of MM/DD/YY: ")
month, day, year = lmp.split("/")
month = int(month)
day = int(day)
year = int(year)
print(month, day, year)