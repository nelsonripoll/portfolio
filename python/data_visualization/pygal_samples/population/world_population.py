import pygal

from collections import OrderedDict
from countries   import WorldPopulation

wp = WorldPopulation("population.json")

data = wp.filter_by_year("2013")

wp.print_map("2013 Population", "americas.svg")

population_groups = OrderedDict()
population_groups["<500m"] = {}
population_groups["500m-1b"] = {}
population_groups[">1b"] = {}

for country_code, population in data.items():
    if int(population) < 500000000:
        population_groups["<500m"].update({country_code: population})

    elif int(population) >= 500000000 and int(population) <= 1000000000:
        population_groups["500m-1b"].update({country_code: population})

    elif int(population) > 1000000000:
        population_groups[">1b"].update({country_code: population})

custom_style = pygal.style.Style(colors=('#0020C2', '#347C17', '#E66C2C')) 
wm = pygal.maps.world.World(style=custom_style)
for group, data in population_groups.items():
    wm.add(group, data)
wm.render_to_file("americas.svg")
