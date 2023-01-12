# PYTHON-14. Очистка данных
# 2. Знакомство с новыми данными: данные о квартирах от Сбера

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.expand_frame_repr', False)

sber_data = pd.read_csv('data/sber_data.csv')

# 2.1
# print(sber_data.shape)
# print(sber_data.info())

cols_null_percent = sber_data.isnull().mean() * 100
cols_with_null = cols_null_percent[cols_null_percent>0].sort_values(ascending=False)
# display(cols_with_null)
# print(cols_with_null)

cols_with_null.plot(
    kind='bar',
    figsize=(10, 4),
    title='Распределение пропусков в данных'
);

# print(sber_data.tail())
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
