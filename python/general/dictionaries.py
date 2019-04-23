# declaring a dictionary
dog = {
      'name': 'Servo',
      'size': 'medium', 
    'weight':  35.4, 
     'color': 'brown'
}

# length
len(dog)

# return value with key
name = dog['name']

# add key and value
dog['fur'] = 'short'

# remove key and value
del dog['size']

# check if key exists (or doesn't exist), returns boolean
'name' in dog
'breed' not in dog

# looping through a dictionary
for key, value in dog.items():
    result = str(key) + ': ' str(value)

# list of keys
dog.keys()

# list of values
dog.values()

# get by key
default = "0"
switcher = {
    1: "1",
    2: "2",
    3: "3"
}
switcher.get(2, default) # second argument is optional

# pop by key
numbers = {
    1: "1",
    2: "2",
    3: "3"
}
item = numbers.pop(1, "")


# update a dictionary
sandwich_1 = {
      'bread': 'wheat',
      'meats': ['turkey', 'ham', 'roast beef'],
    'cheeses': ['swiss'],
      'other': ['baby spinach', 'banana peppers', 'sliced tomatoes', 'honey mustard']
}

additions = {'sides': ['chips', 'pickle', 'cookie']}

sandwich_1.update(additions) # sides key has been added

sandwich_2 = {
      'bread': 'white',
      'meats': ['turkey'],
    'cheeses': ['american cheese'],
      'other': ['lettuce', 'sliced tomatoes', 'mayo']
}

sandwich_1.update(sandwich_2) # sandwich_1 is now equal to sandwich_2
