#Generate a Moore's Law plot.
#Uses data from github.
import urllib.request
import re
import matplotlib.pyplot as plt
import numpy as np
import math


def exponenial_func(x, a, b, c):
    return a*np.exp(b*x)+c

url = 'https://raw.githubusercontent.com/karlrupp/microprocessor-trend-data/master/42yrs/transistors.dat'
print("Fetching data...")
response = urllib.request.urlopen(url)
data = response.read().decode('utf-8')
print("Data fetched.")
print("Generating plot...")
whitespace_split = re.compile(r'[^\S\x0a\x0d]+')
data_mangled = [[float(dpoint) for dpoint in whitespace_split.split(line)] for line in re.compile(r'[\r\n]+').split(re.sub(r'#+\n', '',data.rstrip()))]
plt.scatter(*zip(*data_mangled))
min_x = min([element[0] for element in data_mangled])
max_x = max([element[0] for element in data_mangled])
min_y = min([element[1] for element in data_mangled])
max_y = max([element[1] for element in data_mangled])
plt.axis([min_x, max_x, min_y, max_y])
plt.yscale('log')
plt.xticks([round(i) for i in np.linspace(math.floor(min_x), math.ceil(max_x), 5)])
plt.xlabel('Year')
plt.ylabel('Average Number of Transistors (Thousands)').
plt.savefig('moore.eps', format='eps', dpi=1000)
