#lmp = last menstrual cycle

def main():
    lmp = input("Please enter your last menstrual cycle date in the format of MM/DD/YY: ")
    convert(lmp)
    edd = convert(lmp)
    print(f'Your estimated delivery date is {edd}.')
    
def convert(lmp):
    month, day, year = lmp.split("/")
    month = int(month) -3
    day = int(day) + 7
    year = int(year) + 1
    if float(day) > 30.437:
        adj_day = day - 31
        day = int(adj_day)
    return (f'{month}/{day}/{year}')


main()