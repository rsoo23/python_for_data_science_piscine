
import matplotlib.pyplot as plt
from load_csv import load
import numpy as np


def adjust_pop(pop):
    '''takes in a population, converts the format to millions(M)'''
    if 'k' in pop:
        return float(pop.replace('k', ' ')) / 1000
    elif 'M' in pop:
        return float(pop.replace('M', ' '))
    elif 'B' in pop:
        return float(pop.replace('B', ' ')) * 1000


def main():
    '''main function: creates the plot showing the population projections
    of selected countries
    '''
    try:
        dataframe = load("population_total.csv")

        years = dataframe.columns[1:-50]

        countries = ['Malaysia', 'Germany', 'Singapore',
                     'India', 'Indonesia', 'China']

        pop = [dataframe[dataframe['country'] == c] for c in countries]
        adjusted_pop = [p.iloc[0, 1:-50].apply(adjust_pop) for p in pop]

        # y_tick adjustment
        max_pop = max([max(country_pop) for country_pop in adjusted_pop])
        if max_pop > 1000:
            y_tick_step = 200
        else:
            y_tick_step = 20

        for adj_p, c in zip(adjusted_pop, countries):
            plt.plot(years, adj_p, label=c)
        y_ticks = np.arange(0, max_pop + 20, y_tick_step)
        y_labels = [f'{int(y)}M' for y in y_ticks]
        plt.yticks(y_ticks, y_labels)
        plt.legend(countries, loc='lower right')
        plt.xticks(['1800', '1840', '1880', '1920', '1960', '2000', '2040'])
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.title('Population Projections')
        plt.show()
    except KeyboardInterrupt:
        pass
    except IndexError:
        print("IndexError: country not found")


if __name__ == "__main__":
    main()
