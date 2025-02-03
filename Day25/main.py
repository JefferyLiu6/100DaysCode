import pandas as pd

df = pd.read_csv("./Day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv") 

print(df["Primary Fur Color"].unique())

gray = df[df["Primary Fur Color"]=="Gray"]
print(gray["Unique Squirrel ID"].count())

red = df[df["Primary Fur Color"]=="Cinnamon"]
print(red["Unique Squirrel ID"].count())

black = df[df["Primary Fur Color"]=="Black"]
print(black["Unique Squirrel ID"].count())

data_dict = {
    "Fur Color" : ["Gray", "Red", "Black"],
    "Count" : [gray["Unique Squirrel ID"].count(), red["Unique Squirrel ID"].count(), black["Unique Squirrel ID"].count()]
}

data = pd.DataFrame(data_dict)
data.to_csv("./Day25/count.csv")