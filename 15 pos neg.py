positive_sum = 0
positive_count = 0
negative_sum = 0
negative_count = 0

while True:
    num = int(input("Enter a number (-1 to stop): "))
    if num == -1:
        break
    elif num > 0:
        positive_sum += num
        positive_count += 1
    elif num < 0:
        negative_sum += num
        negative_count += 1

if positive_count > 0:
    positive_avg = positive_sum / positive_count
    print(f"Average of positive numbers: {positive_avg:.2f}")
else:
    print("No positive numbers entered.")

if negative_count > 0:
    negative_avg = negative_sum / negative_count
    print(f"Average of negative numbers: {negative_avg:.2f}")
else:
    print("No negative numbers entered.")
