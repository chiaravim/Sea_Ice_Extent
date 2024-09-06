import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# x axis, years

x = numbers_list = list(range(1, 46))

# y axis, amount per year (avg)

y = [12663, 12207, 12229, 12054, 12547, 12367, 11790, 12000, 12249, 11401, 12096, 11991, 11609, 11746, 11974, 11969, 11958, 11346, 11754, 11597, 11794, 11641, 11439, 11563, 11349, 11439, 11297, 10902, 10680, 10508, 10951, 10908, 10664, 10541, 10367, 10901, 10923, 10569, 10104, 10381, 10413, 10177, 10166, 10383, 10594]

plt.style.use("seaborn")
plt.bar(x=x, height=y, width=0.4)
plt.xticks([2,23,44], ["1980","2000","2020"])

plt.plot(x,y,color="green")
plt.xlabel('Years')
plt.ylabel('Sea Ice Extent in million m^2')
plt.title("Sea Ice Index From 1978 to 2022")

plt.show()
