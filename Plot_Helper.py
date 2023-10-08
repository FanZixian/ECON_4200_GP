import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def yield_curve_plot(df, date):
    # This function is to plot the yield curve at a specific date
    yields_value = df.loc[date, :]
    length = len(yields_value.values)
    print(length)
    
    plt.figure(figsize = (10, 8))
    plt.plot(yields_value, color = 'blue', label = 'Treasury Bond Yield Curve', marker = 'o')
    plt.legend()

    plt.grid()
    plt.show()

