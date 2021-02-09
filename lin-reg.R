df <- read.csv("./Advertising.csv")
plot(df)
plot(TV~sales,data=df)
fit<- lm(sales~TV+radio+newspaper,data=df)
test.data <- data.frame(TV=75,newspaper=75,radio=75)
predict(fit,newdata=test.data,interval="prediction")

