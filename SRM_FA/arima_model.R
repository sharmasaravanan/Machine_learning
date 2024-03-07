library(forecast)
library(ggplot2)

data <- read.table("./TSLA.csv", sep=',', header=T)
measure <- data$Close

# the last 54 days are for testing
measure_test <- measure[200:253]

# The first 199 days are for training
measure <- measure[1:199]

# Fit an ARIMA model
fit <- arima(ts(measure), c(10, 1, 5))
fore <- forecast(fit, 54)

mean(abs(fore$mean - measure_test)) # MAE
cor(fore$mean, measure_test) # Correlation (square it to get R-squared)

p <- ggplot()
p <- p + geom_line(aes(x=1:199, y=measure, color="Original Data"))
p <- p + geom_line(aes(x=200:253, y=measure_test, color="Original Data TEST"))
p <- p + geom_line(aes(x=200:253, y=fore$mean, color="Predicted using Arima"))
p <- p + ylab("Value of the Stock")
p <- p + xlab("Time in Days")
p <- p + ggtitle("Stock Price Prediction using Arima")
p <- p + geom_ribbon(aes(x=c(200:253), y = fore$mean, ymin=fore$lower[,2], ymax=fore$upper[,2]), linetype=2, alpha=0.1)
print(p)
