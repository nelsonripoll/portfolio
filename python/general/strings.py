#!/usr/bin/python3

# text manipulation
message = "Hello world"
message.title() # Hello World
message.upper() # HELLO WORLD
message.lower() # hello world

# concatenations and escape characters
first = "Hello"
last  = "World"
 
message = first + " " + last # "Hello World"

# strip whitespaces
message = " this message has extra spaces "

message.rstrip() # " this message has extra spaces"
message.lstrip() # "this message has extra spaces "
message.strip()  # "this message has extra spaces"

num = 5
message = "I have " + str(num) + " cookies"
