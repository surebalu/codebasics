num = input("Enter a number that you want to check: ")
try:
    num = int(num)
    print(type(num))
    if num % 2 == 0:
        print(f"{num} is even number")
    else:
        print(f"{num} is odd number")
except ValueError:
    print("Enter a numeric value")

indian = ["samosa", "idli", "dosa"]
mexican = ["burrito", "bowl", "fajitas"]
italian = ["pasta", "pizza", "risotto"]

dish = input("Please enter your fav dish:: ")

if dish in indian:
    print(f"{dish} is indian")
elif dish in mexican:
    print(f"{dish} is mexican")
elif dish in italian:
    print(f"{dish} is italian")
else:
    print(f"I dont know what kind of dish is {dish}")

