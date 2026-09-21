Temperature=float(input("Enter temperature"))
if Temperature<0:
    print("TEmperature is Freezing")
elif Temperature<=15:
    print("Temperature is Very Cold")
elif Temperature<=25:
    print("Temperature is Cold")
elif Temperature<=35:
    print("Temperature is Normal")
elif Temperature<=45:
    print("Temperature is Hot")
else:
    print("Temperature is Extremely Hot")
