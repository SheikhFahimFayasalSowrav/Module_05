'''The comfortable relative humidity for humans is between 40% and 60%.
Write a program that will take input todays humidity in the variable “hum”.
Then complete the code to output "norm" if the taken percent of humidity is
in the range of 40 and 60 inclusive. Output “High” when exceeds 60% and
“Low” when less than 40%. Output “ERROR Input” when the input is wrong.'''

hum = float(input("Please enter only floating point: "))

if hum >= 40 and hum <= 60:
    print("norm")
    if hum < 0 or hum > 100:
        print("Error Input")

elif hum < 40:
    print("Low")
    if hum < 0 or hum > 100:
        print("Error Input")

elif hum > 60:
    print("High")
    if hum < 0 or hum > 100:
        print("Error Input")

#Leap Year

year = int(input("Enter Year: "))
#Leap Year Check

if year % 4 == 0 and year % 100 != 0:
    print(year, "is a Leap Year")
elif year % 100 == 0:
    if year % 400 == 0:
        print(year, "is a Leap Year")
    else:
        print(year, "is not a Leap Year")
else:
    print(year, "is not a Leap Year")


