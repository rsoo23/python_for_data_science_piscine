
import matplotlib.pyplot as plt
from load_csv import load


def main():
    '''main function: creates the plot showing the life expectancy
    projections of the selected country
    '''
    try:
        dataframe = load("life_expectancy_years.csv")

        country_name = 'Malaysia'

        # alternative:
        # in load_csv, use dataframe = pd.read_csv(path, index_col=0)
        # country_data = dataframe.loc[country]
        # country_data.plot()

        country_data = dataframe[dataframe['country'] == country_name]
        years = dataframe.columns[1:]
        life_expectancy = country_data.iloc[0, 1:]
        plt.plot(years, life_expectancy)

        plt.xticks(['1800', '1840', '1880', '1920',
                    '1960', '2000', '2040', '2080'])
        plt.xlabel('Year')
        plt.ylabel('Life Expectancy')
        plt.title(country_name + ' Life Expectancy Projections')
        plt.show()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
