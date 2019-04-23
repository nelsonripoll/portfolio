import csv

from matplotlib import pyplot   as plt
from datetime   import datetime as dt

filename = 'weather_stats.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = dt.strptime(row[0], "%Y-%m-%d")
            high = int(float(row[1]))
            low  = int(float(row[3]))
        except ValueError:
            print(current_date, "missing data")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low) 
    fig = plt.figure(dpi=128, figsize=(10,6))

    plt.plot(dates, 
             highs, 
             label="highs", 
             color="red", 
             linewidth=1,
             alpha=0.5)

    plt.plot(dates, 
             lows, 
             label="lows", 
             color="blue", 
             linewidth=1,
             alpha=0.5)

    plt.legend(fontsize=10, frameon=False)

    plt.fill_between(dates, highs, lows, facecolor="purple", alpha=0.1)

    plt.title("2015 Daily high/low temeratures - 78154", fontsize=14)
    plt.xlabel("", fontsize=10)
    fig.autofmt_xdate()
    plt.ylabel("Temerature (f)", fontsize=10)
    plt.tick_params(axis="both", which="major", labelsize=10)

    plt.show()
    # plt.savefig("graph.png")
