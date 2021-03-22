from ggplot import *
from random import *
from matplotlib import *
from pandas import *
def prettyggplotGraph(data):
    title = "Population of Elysee"
    plot = ggplot(data, aes(x='time', y='population')) + geom_line()
def matplotPlot(data):
    pyplot.plot('time', 'population', data = data)
def main():
    pop = 107836055
    data = []
    year = 0
    while(year != 987):
        data.append([pop, year])
        pop *= 2
        year += 1
    data = pandas.DataFrame(data, columns=['population', 'time'])
    prettyggplotGraph(data)
    matplotPlot(data)
main()
