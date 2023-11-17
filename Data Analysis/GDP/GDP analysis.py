###### Libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

###### CSV

df = pd.read_csv(r"C:\Users\Nicho\Desktop\GDP.csv")

###### Data Exploration

print(df.describe())
print(df.isnull().sum())
print(df.duplicated().sum()) #The dataset does not have any duplicates

###### Data Cleaning

df = df.dropna()

###### Data Distribution

df["gdp"].hist(bins=20, edgecolor="black")
plt.title("Distribution of GDP")
plt.xlabel("GDP")
plt.ylabel("Frequency")
plt.show()

df.boxplot(column="gdp")
plt.title("Boxplot of GDP")
plt.show()

plt.figure(figsize=(6, 5))
df["country"].nunique()
df["country"].value_counts().plot(kind="bar")
plt.title("Number of Data points per Country")
plt.xlabel("Country")
plt.xticks(rotation=45, ha="right")
plt.ylabel("Count")
plt.show()

###### EDA

## Continents

regions1 = ['European Union', 'North America', 'East Asia & Pacific',
       'Latin America & Caribbean', 'Middle East & North Africa']

for region in regions1:
    df[df["country"] == region].groupby("year")["pop"].sum().plot()
plt.legend(regions1)
plt.show()

for region in regions1:
    df[df["country"] == region].groupby("year")["pop_over_65"].sum().plot()
plt.legend(regions1)
plt.show()

for region in regions1:
    df[df["country"] == region].groupby("year")["unemployment_r"].sum().plot()
plt.legend(regions1)
plt.show()

for region in regions1:
    df[df["country"] == region].groupby("year")["gdp_over_pop"].sum().plot()
plt.legend(regions1)
plt.show()


## European Union

West_EU = ["France", "Germany", "Ireland", "Italy",
      "Portugal", "Spain", "Switzerland", "United Kingdom"]

for region in West_EU:
    df[df["country"] == region].groupby("year")["pop"].sum().plot()
plt.legend(West_EU)
plt.show()

for region in West_EU:
    df[df["country"] == region].groupby("year")["gdp_over_pop"].sum().plot()
plt.legend(West_EU)
plt.show()

EU = ["Albania", "Andorra", "Armenia", "Austria", "Azerbaijan", "Belarus", "Belgium",
          "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus", "Czechia", "Denmark",
          "Estonia", "Finland", "France", "Georgia", "Germany", "Greece", "Hungary", "Iceland",
          "Ireland", "Italy", "Kazakhstan", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg",
          "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", "North Macedonia", "Norway",
          "Poland", "Portugal", "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia",
          "Spain", "Sweden", "Switzerland", "Ukraine", "United Kingdom", "Armenia", "Azerbaijan", "Georgia", "Russia", "Turkiye"]

Rich_EU = df[df["country"].isin(EU)].groupby("country")["gdp_over_pop"].max().sort_values(ascending=False).reset_index().head(10)
ax = sns.barplot(data=Rich_EU, x="country", y="gdp_over_pop")
plt.xticks(rotation=45, horizontalalignment="right")
plt.title("Highest GDP per capita in Europe")
for index, row in Rich_EU.iterrows():
    ax.text(row.name, row["gdp_over_pop"], "$"+str(int(row["gdp_over_pop"]))[:-3]+"k", color="black", ha="center", va="bottom")
plt.show()

Poor_EU = df[df["country"].isin(EU)].groupby("country")["gdp_over_pop"].mean().sort_values().reset_index().head(10)
ax = sns.barplot(data=Poor_EU, x="country", y="gdp_over_pop")
plt.xticks(rotation=45, horizontalalignment="right")
plt.title("Lowest GDP per capita in Europe")
for index, row in Poor_EU.iterrows():
    ax.text(row.name, row["gdp_over_pop"], "$"+str(int(row["gdp_over_pop"]))[:-3]+"k", color="black", ha="center", va="bottom")
plt.show()


## World

World = df.groupby("country")["gdp_over_pop"].max().sort_values(ascending=False).reset_index().head(10)
ax = sns.barplot(data=World, x="country", y="gdp_over_pop")
plt.xticks(rotation=45, horizontalalignment="right")
plt.title("Highest GDP per capita in the World")
for index, row in World.iterrows():
    ax.text(row.name, row["gdp_over_pop"], "$"+str(int(row["gdp_over_pop"]))[:-3]+"k", color="black", ha="center", va="bottom")
plt.show()

World_unemployment = df.groupby("country")["unemployment_r"].mean().sort_values(ascending=False).reset_index().head(10)
ax = sns.barplot(data=World_unemployment, x="country", y="unemployment_r")
plt.xticks(rotation=45, horizontalalignment="right")
plt.title("Highest unemployment rate in the World")
for index, row in World_unemployment.iterrows():
    ax.text(row.name, row["unemployment_r"], str(int(row["unemployment_r"]))+"%", color="black", ha="center", va="bottom")
plt.show()

World_lowest_unempl = df.groupby("country")["unemployment_r"].mean().sort_values().reset_index().head(10)
ax = sns.barplot(data=World_lowest_unempl, x="country", y="unemployment_r")
plt.xticks(rotation=45, horizontalalignment="right")
plt.title("Lowest unemployment rate in the World")
for index, row in World_lowest_unempl.iterrows():
    ax.text(row.name, row["unemployment_r"], str(round(row["unemployment_r"], 2))+"%", color="black", ha="center", va="bottom")
plt.show()







