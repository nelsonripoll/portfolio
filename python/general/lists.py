# list
foods = ['apples', 'pizza', 'sushi', 'chips', 'apricots', 'yogurt', 'bananas']
foods.reverse()  # ['chips', 'sushi', 'pizza', 'apples']

# length of list
len(foods) # 4

# accessing elements
foods[0]    # apples
foods[2]    # sushi
foods[-1]   # chips

# changing elements
foods[0] = 'waffles'

# adding elements
foods.append('cookies')   # add to the end of the list
foods.insert(1, 'apples') # insert at index

# removing elements
del foods[4]
foods.remove('pizza')

# pop
popped_food = foods.pop()   # from the end of the list
popped_food = foods.pop(1)  # from index

# sort
foods.sort()
foods.sort(reverse=True)
sorted(foods)

# loop through a list
for food in foods:
    pass

while foods:
    foods.pop()

# numerical lists
for num in range (1,5): # range (start, stop)
    pass

numbers      = list(range(1,6))
even_numbers = list(range(2, 11, 2))
odd_numbers  = list(range(1, 10, 2))
min(numbers) # 1
max(numbers) # 5
sum(numbers) # 15

# list comprehension
cubes = [value**3 for value in range(1,11)] 
# cubes = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

# slicing lists
cubes[1:5] # [8, 27, 64, 125]
cubes[:4]  # [1, 8, 27, 64]
cubes[4:]  # [125, 216, 343, 512, 729, 1000]
cubes[-4:] # [343, 512, 729, 1000]

# lists sharing memory
copy_cubes = cubes
copy_cubes.append(11**3)
# cubes, copy_cubes = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331]

# copying lists
copy_cubes = cubes[:]
copy_cubes.append(11**3)
# cubes = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
# copy_cubes = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331]
