import pygal
import random

from die import Die

dice = [4, 6, 8, 10, 12, 20] 

die_1 = Die(random.choice(dice))
die_2 = Die(random.choice(dice))
die_3 = Die(random.choice(dice))

die_label = die_1.get_name() + '+' + die_2.get_name() + '+' + die_3.get_name()
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides

results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

frequencies = []
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.title = die_label + " after 1000 rolls"
hist.x_labels = [x for x in range(3, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add(die_label, frequencies)
hist.render_to_file(die_label + '.svg')
