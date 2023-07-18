A = int(input("Enter the decimal number A: "))
B = int(input("Enter the base B: "))

result = ""

while A > 0:
    remainder = A % B
    result = str(remainder) + result
    A //= B

print(result)
