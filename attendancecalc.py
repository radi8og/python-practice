total = int(input("Enter total classes conducted:"))
attended = int(input("Enter classes attended:"))

percentage = (attended / total) * 100

print("Attendance Percentage:", round(percentage,2), "%")

if percentage >= 30:
    print ("You have safe attendance.")
else:
    needed = 0

    while (attended + needed) / (total + needed) < 0.30:
        needed += 1
    
    print("You need to attend", needed, "more classes to reach 30%.")

