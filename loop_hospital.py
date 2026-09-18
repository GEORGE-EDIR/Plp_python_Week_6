# Patient 1
# FIXED: range(1, 10) stops before 10, so the stop value must be 11.
for i in range(1, 11):
    print(i)

# Patient 2
# FIXED: n must decrease inside the while loop so that it eventually stops.
n = 3
while n > 0:
    print(n)
    n = n - 1

# Patient 3
# FIXED: total must be initialized before the loop so each iteration adds to the previous total.
total = 0
for i in range(1, 6):
    total = total + i

print(total)