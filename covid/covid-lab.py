"""
С сайта https://data.humdata.org/dataset/novel-coronavirus-2019-ncov-cases
собрать статистику по заболеваемости, выздоровлению и смертям

"""


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.dates import DateFormatter




df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv',
                 parse_dates=['Date'])
countries = ['Canada', 'Germany', 'United Kingdom', 'US', 'France', 'China']
df = df[df['Country'].isin(countries)]


df['Cases'] = df[['Confirmed', 'Recovered', 'Deaths']].sum(axis=1)


"""Поворачиваем наш фрейм данных df, создавая столбцы из стран с количеством дел в качестве полей данных. 
Этот новый фрейм данных называется covid. Затем мы устанавливаем индекс данных в качестве даты и 
назначаем названия стран заголовкам столбцов."""
df = df.pivot(index='Date', columns='Country', values='Cases')
countries = list(df.columns)
covid = df.reset_index('Date')
covid.set_index(['Date'], inplace=True)
covid.columns = countries


"""мы копируем наш датафрейм covid и называем его percapita. 
Мы используем словарь, в котором хранится население всех наших стран, и делим каждое значение 
на население и умножаем его на 100 000, чтобы сгенерировать количество случаев на 100 000 человек."""
populations = {'Canada': 37664517, 'Germany': 83721496, 'United Kingdom': 67802690, 'US': 330548815, 'France': 65239883,
               'China': 1438027228}
percapita = covid.copy()
for country in list(percapita.columns):
    percapita[country] = percapita[country] / populations[country] * 100000


colors = {'Canada': '#045275', 'China': '#089099', 'France': '#7CCBA2', 'Germany': '#FCDE9C', 'US': '#DC3977',
          'United Kingdom': '#7C1D6F'}
plt.style.use('fivethirtyeight')


plot = covid.plot(figsize=(12, 8), color=list(colors.values()), linewidth=5, legend=False)
plot.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
plot.grid(color='#d4d4d4')
plot.set_xlabel('Date')
plot.set_ylabel('# of Cases')


for country in list(colors.keys()):
    plot.text(x=covid.index[-1], y=covid[country].max(), c=colors[country], s=country, weight='bold')


plot.text(x=covid.index[1], y=int(covid.max().max()) + 45000, s="COVID-19 Cases by Country", fontsize=23, weight='bold',
          alpha=.75)
plot.text(x=covid.index[1], y=int(covid.max().max()) + 15000,
          s="For the USA, China, Germany, France, United Kingdom, and Canada\nIncludes Current Cases, Recoveries, and Deaths",
          fontsize=16, alpha=.75)
plot.text(x=percapita.index[1], y=-100000,
          s='datagy.io                      Source: https://github.com/datasets/covid-19/blob/master/data/countries-aggregated.csv',
          fontsize=10)

percapitaplot = percapita.plot(figsize=(12, 8), color=list(colors.values()), linewidth=5, legend=False)
percapitaplot.grid(color='#d4d4d4')
percapitaplot.set_xlabel('Date')
percapitaplot.set_ylabel('# of Cases per 100,000 People')
for country in list(colors.keys()):
    percapitaplot.text(x=percapita.index[-1], y=percapita[country].max(), c=colors[country], s=country, weight='bold')
percapitaplot.text(x=percapita.index[1], y=percapita.max().max() + 25, s="Per Capita COVID-19 Cases by Country",
                   fontsize=23, weight='bold', alpha=.75)
percapitaplot.text(x=percapita.index[1], y=percapita.max().max() + 10,
                   s="For the USA, China, Germany, France, United Kingdom, and Canada\nIncludes Current Cases, Recoveries, and Deaths",
                   fontsize=16, alpha=.75)
percapitaplot.text(x=percapita.index[1], y=-55,
                   s='datagy.io                      Source: https://github.com/datasets/covid-19/blob/master/data/countries-aggregated.csv',
                   fontsize=10)

plt.show()