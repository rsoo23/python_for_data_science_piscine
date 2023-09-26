
import matplotlib.pyplot as plt
from load_csv import load


def main():
    '''displays a scatter plot of with GDP on the x-axis and life expectancy
    on the y-axis
    '''
    try:
        df_life = load("life_expectancy_years.csv")
        df_gdp = \
            load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

        life_exp = df_life['1900']
        gdp = df_gdp['1900']

        plt.scatter(gdp, life_exp)
        plt.xlabel('Gross Domestic Product')
        plt.ylabel('Life Expectancy')
        plt.xscale('log')
        plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
        plt.title('1900')
        plt.show()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
