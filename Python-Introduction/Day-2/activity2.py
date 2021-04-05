while True:
    try:
        fee = float(input("Fee: "))
    except ValueError:
        print("Please input a number")
        continue
    try:
        tip = float(input("Tip Percentage: "))
    except ValueError:
        print("Please input a number")
        continue
    final_tip = tip / 100
    total = fee * final_tip
    break
    
print(f"Tip: {total}")