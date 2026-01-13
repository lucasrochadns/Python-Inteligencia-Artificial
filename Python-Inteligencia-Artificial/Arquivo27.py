def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

user_number = int(input("Insert Number "))
print(f' Fatorial {user_number} e {fatorial(user_number)}')