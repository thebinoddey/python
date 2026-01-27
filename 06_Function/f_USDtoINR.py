def conversion(val):
    val = val * 87.87
    return val

usd = float(input("Enter amount in USD: "))
print(f"The amount in INR is: {conversion(usd)}")
    