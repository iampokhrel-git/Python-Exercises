def calculate_squareroot(num,precision=0.00001):
    
    if num<0:
        raise valueerror("cannot calculate of negative number.")
    guess=num / 2
    while abs(guess**2 - num)> precision:
        guess = (guess+num / guess) / 2
    
    return guess
num = float(input("enter a number"))
sqrt = calculate_squareroot(num)
print(f"the square root of {num} is : {sqrt}")
