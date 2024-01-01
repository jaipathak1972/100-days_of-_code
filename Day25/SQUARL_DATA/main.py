import pandas

Data = pandas.read_csv("Day25/SQUARL_DATA/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey =(len(Data[Data["Primary Fur Color"]=="Gray"]))
black=(len(Data[Data["Primary Fur Color"]=="Black"]))
cinnamon=(len(Data[Data["Primary Fur Color"]=="Cinnamon"]))


dict = {
    
    "color" : ["Grey","Black","Cinnamon"],
    "scores": [grey,black,cinnamon]
}

data=pandas.DataFrame(dict)
data.to_csv("new_Data.csv")