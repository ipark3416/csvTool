import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('test.csv')

col_options = df.columns.tolist()


y_data_ind = int(input(f"Which column would you like to plot on the y-axis? \nOptions: \n{ ' \n'.join(f'[{i}] {col}' for i, col in enumerate(col_options))} \n "))
x_data_ind = int(input(f"Which column would you like to plot on the x-axis? \nOptions: \n{ ' \n'.join(f'[{i}] {col}' for i, col in enumerate(col_options))} \n "))

df.plot(x=col_options[x_data_ind], y=col_options[y_data_ind])

plt.title(f"{col_options[y_data_ind]} vs {col_options[x_data_ind]}")
plt.xlabel(col_options[x_data_ind])
plt.ylabel(col_options[y_data_ind])


plt.show()



