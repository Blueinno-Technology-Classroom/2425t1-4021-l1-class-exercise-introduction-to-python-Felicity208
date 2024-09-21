# >>Input a year: ???
# >>This is /is not a leap year.
# >>Input a year: 2004
# >>This is a leap year.
# >>Input a year: 2100
# >>This is not a leap year.
year = int(input("input a year: "))

if year % 400 == 0:
    print("This is a leap year.")
elif year % 4 == 0 and not(year % 100 == 0):
    print("This is a leap year.")
else:
    print("This is not a leap year.")
