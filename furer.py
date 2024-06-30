import pandas as pd
# df = pd.read_csv("GoogleApps.csv")

df = pd.read_csv("GooglePlayStore_wild.csv")
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

# mmm = df[df["Rating"] > 4.5]["Category"].value_counts
# print(mmm["FINANCE"])

# print(len(df[pd.isnull(df["Rating"])]))
# df["Rating"].fillna(1,inplace=True)

print(df[df["Category"]=="TOOLS"]["Size"].value_counts().sort_values())