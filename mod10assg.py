from ggplot import *
from random import *
from matplotlib import *
from pandas import *
def ggplotGraph(data):
    ggplot(data, aes(x='time', y='population')) + geom_line()
def matplotPlot(data):
    pyplot.plot('time', 'population', data = data)
def main():
    pop = 107836055
    data = []
    year = 0
    while(year != 783):
        data.append([pop, year])
        pop *= 1 + random()
        year += 1
    data = pandas.DataFrame(data, columns=['population', 'time'])
    ggplotGraph(data)
    matplotPlot(data)
    print(data)
main()
