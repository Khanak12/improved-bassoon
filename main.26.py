while True:
    try:
        age = int(input("Enter your age: "))
        if age <= 0:
            raise ValueError("Age cannot be negative or zero.")
        break
    except ValueError as e:
        print(f"Invalid age entered: {e}")

if age % 2 == 0:
    print(f"Your age is {age} and it is even.")
else:
    print(f"Your age is {age} and it is odd.")