x = int(input())
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
for i in range(1, 13):
     if (x == i):
          print(months[i - 1])