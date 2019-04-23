import pygal
import random

from die import Die

dice = [4, 6, 8, 10, 12, 20] 
die = Die(random.choice(dice))

die_label = die.get_name()
max_result = die.num_sides

results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []

for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.title = die_label + " after 1000 rolls"
hist.x_labels = [x for x in range(1, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add(die_label, frequencies)
hist.render_to_file(die_label + '.svg')
