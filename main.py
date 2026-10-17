import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import sys

run = 1

filename = input("What is the name of your CSV file (do not add the .csv suffix)? \n")

df = pd.read_csv("csv_files/" + filename + ".csv", encoding = 'cp1252')

col_options = df.columns.tolist()
while (run):
    y_data_ind = int(input(f"Which column would you like to plot on the y-axis? \nOptions: \n{ ' \n'.join(f'[{i}] {col}' for i, col in enumerate(col_options))} \n "))
    x_data_ind = int(input(f"Which column would you like to plot on the x-axis? \nOptions: \n{ ' \n'.join(f'[{i}] {col}' for i, col in enumerate(col_options))} \n "))

    save = input("Would you like to save your plot? [y/n] \n")
    show = input("Would you like to show your plot before saving? [y/n] \n")

    df.plot(x=col_options[x_data_ind], y=col_options[y_data_ind],kind="scatter",figsize=(11,5),s=7, color = "blue", marker = "s")

   

    plt.title(f"{col_options[y_data_ind]} vs {col_options[x_data_ind]}")
    plt.xlabel(col_options[x_data_ind])
    plt.ylabel(col_options[y_data_ind])


    if(save=="y"):
        plt.savefig("saved/"f"{col_options[y_data_ind]} vs {col_options[x_data_ind]}")

    if(show=="y"):
        plt.show()


    exit = input("Input 0 to exit or press enter to generate another plot: \n")
    if(exit=="0"):
        sys.exit(0)