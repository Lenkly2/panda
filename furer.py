import pandas as pd
df = pd.read_csv("GoogleApps.csv")

# adolf = df["Content Rating"].value_counts()
# print(adolf)
# gitler = adolf["Teen"] / adolf["Everyone 10+"]
# print(gitler)
# print(df["Category"].value_counts())
# print(nigger)


#seredne = df.groupby(by="Type")["Rating"].mean()
#print(seredne["Paid"] - seredne["Free"])

# comycs = df.groupby(by="Category")["Size"].min()
# print(comycs)
# comycs = df.groupby(by="Category")["Size"].agg(["min", "max"])
# print(comycs)

mmm = df[df["Rating"] > 4.5]["Category"].value_counts
print(mmm["FINANCE"])