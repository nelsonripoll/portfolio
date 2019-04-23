# if statement
flag = True

if flag == True:
    pass
elif flag == False:
    pass
else:
    pass


# for loop with list
for food in range(1, 11): # 1 - 10
    pass


# for loop break and else
prime = False

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            prime = False
            break
    else: # only runs if no break occurs
        prime = True


# for loop continue
even = False

for n in range(2, 10):
    if n % 2 == 0:
        even = True
        continue

    even = False


# while loop conditional
i = 0
while i < 10:
    i += 1


# while loop flag
i = 0
flag = True

while flag:
    if i == 10:
        flag = False
    else:
        i += 1


# while loop break
i = 0
while True:
    if i == 10:
        break
    else:
        i += 1


# while loop continue
i = 0

while i < 10:
    i += 1

    if i % 2 == 0:
        continue
   
    pass
