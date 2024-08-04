import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

a = df[df["gender"] == "male"]["math score"].value_counts()
a.plot(kind = "pie")

# b = df[df["parental level of education"] == "some college"]["reading score"].value_counts()
# b.plot(kind = "pie")

# c = df[(df["gender"] == "female") & (df["race/ethnicity"] == "group B")]["math score"].value_counts()
# c.plot(kind = "pie")
plt.show()
