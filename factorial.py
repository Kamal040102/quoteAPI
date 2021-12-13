def fact(n):
    try:
        if n == 1 or n ==0:
            return 1
        else:
            return n * fact(n - 1)
    except Exception as e:
        print(e)

userInp = int(input("Enter a number to find the factorial:\t"))
print(fact(userInp))