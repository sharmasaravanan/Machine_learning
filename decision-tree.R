install.packages("party")

library(party)

out <- ctree(play~outlook+ temperature+ humidity+ wind,data=df2)

df1 <- read.csv("./weather.csv")

