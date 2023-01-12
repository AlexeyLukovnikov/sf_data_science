# PYTHON-14. Очистка данных
# 2. Знакомство с новыми данными: данные о квартирах от Сбера

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.expand_frame_repr', False)

sber_data = pd.read_csv('data/sber_data.csv')


# print(sber_data.isnull().tail())
# 2.1

cols_null_percent = sber_data.isnull().mean() * 100
cols_with_null = cols_null_percent[cols_null_percent > 0].sort_values(ascending=False)
# print(cols_with_null)
cols_with_null.plot(
    kind='bar',
    figsize=(10,4),
    title="Empty data"
);
# print(sber_data.info())
# print(sber_data.tail())
# print(sber_data.isnull().tail())

# 2.2
# sber_data = sber_data.groupby(by='sub_area').count()
# print(sber_data.info())
# print(sber_data.describe())
# print(sber_data.head())

# 2.3
# print(sber_data['price_doc'].max())
# print(sber_data['price_doc'].nlargest(5))

# 2.4

# boxplot = sns.boxplot(
#     data = sber_data,
#     x='price_doc',
#     #orient='h',
#     y='ecology'
# )

# 2.5
# scatterplot = sns.scatterplot(
#     data = sber_data,
#     y='price_doc',
#     x='kremlin_km',
#     # hue='species',
#     s=100,
#     # size='sex',
#     sizes=(50, 300)
#
# )
# scatterplot.set_title('Зависимость цены от расстояния до кремял ', fontsize=16)
# scatterplot.set_xlabel('Расстояние до кремля, км')
# scatterplot.set_ylabel('Цена')
# #
# # Постройте диаграмму рассеяния, которая покажет, как цена на квартиру (price_doc) связана с расстоянием до центра Москвы (kremlin_km). В
#
# plt.show()