install.packages("forecast")
library(forecast)
data("AirPassengers")
print(start(AirPassengers))
print(end(AirPassengers))
print(sum(is.na(AirPassengers)))
print(summary(AirPassengers))
plot(AirPassengers)
tsdata <- ts(AirPassengers, frequency = 12) 

ddata <- decompose(tsdata, "multiplicative")

plot(ddata)

plot(AirPassengers)

abline(reg=lm(AirPassengers~time(AirPassengers)))

mymodel <- auto.arima(AirPassengers)

myforecast <- forecast(mymodel, level=c(95), h=10*12)

plot(myforecast)


print(Box.test(mymodel$resid, lag=5, type="Ljung-Box"))
Box.test(mymodel$resid, lag=10, type="Ljung-Box")
Box.test(mymodel$resid, lag=15, type="Ljung-Box")