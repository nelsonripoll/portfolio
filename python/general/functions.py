# defining a function
def hello_world():
    """Display 'Hello, World!' when called."""
    print("Hello, World!")

# calling a function
hello_world()


# defining a function with a parameter 
def echo_func(param1):
    """Print string parameter when called."""
    print(param1)

arg1 = "Waffles"
echo_func(arg1)


# positional arguments, keyword arguments, and default values
def strconcat(param1, param2='Bananas'): # param2 is optional
    """
    Return parameters concatenated in order received.
    Param2 defaults to 'Bananas'.
    """
    return param1 + " & " + param2

# positional
print(strconcat("Apples", "Bananas"))
print(strconcat("Bananas", "Apples"))

# keyword
print(strconcat(param1="Waffles", param2="Blueberries"))
print(strconcat(param2="Blueberries", param1="Waffles"))

# default values
print(strconcat("Strawberries"))


# arbitrary number of arguments
def read_books(books_read, *books): # *books is an empty tuple
    """Add books read to list of books"""
    for book in books:
        books_read.append(book) # lists passes retain changes after function call

books_read = []

read_books(books_read, 'Battle Royale', 'A Game of Thrones')    
# books_read = ['Battle Royale', 'A Game of Thrones']

read_books(books_read, '1984', 'Dune', 'Bram Stoker\'s Dracula')    
# books_read = ['Battle Royale', 'A Game of Thrones', '1984', 'Dune', "Bram Stoker's Dracula"]

read_books(books_read, 'Choke')    
# books_read = ['Battle Royale', 'A Game of Thrones', '1984', 'Dune', "Bram Stoker's Dracula", 'Choke']


def user_info(first_name, last_name, **details): # **details is an empty dictionary
    """Create dictionary of user information."""
    info = {}
    info['first_name'] = first_name
    info['last_name']  = last_name

    for key, value in details.items():
        info[key] = value

    return info

user = user_info("Nelson", "Ripoll", 
                 favorite_food="waffles", 
                 consoles_owned=["snes", "nes", "playstation", "sega"],
                 phone="555-5555",
                 email="test@email.com")

# user = {'first_name': 'Nelson', 
#         'last_name': 'Ripoll',  
#         'favorite_food': 'waffles', 
#         'consoles_owned': ['snes', 'nes', 'playstation', 'sega'],
#         'phone': '555-5555', 
#         'email': 'test@email.com'}

user = user_info("Some", "Person", 
                 fax="444-4444",
                 work_email="contact@email.com")

# user = {'first_name': 'Some', 
#         'last_name': 'Person',  
#         'fax': '444-4444', 
#         'work_email': 'contact@email.com'}
