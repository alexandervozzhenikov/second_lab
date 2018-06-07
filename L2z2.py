n = int(input("n="))
print((n % 3 == 0 and n % 9 != 0) or (n % 4 == 0 and n % 5 == 0 and n % 24 == 0))