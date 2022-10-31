
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("coding-environment-exercise.csv")
df[0:]

plt.plot(df["date"],df["value"])
plt.xticks(rotation=90)
plt.show()



