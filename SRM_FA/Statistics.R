# Load necessary libraries
library(dplyr)
# install.packages("forecast")

df <- data.frame(
  date = seq(as.Date("2023-01-01"), by = "day", length.out = 100),
  value = rnorm(100, mean = 100, sd = 10)
)

# Calculate descriptive statistics
mean_value <- mean(df$value)
median_value <- median(df$value)
sd_value <- sd(df$value)
min_value <- min(df$value)
max_value <- max(df$value)

# Print descriptive statistics
cat("Mean:", mean_value, "\n")
cat("Median:", median_value, "\n")
cat("Standard Deviation:", sd_value, "\n")
cat("Minimum Value:", min_value, "\n")
cat("Maximum Value:", max_value, "\n")


# time series
# Example start and end date for time series analysis
year_start <- 2023
month_start <- 1
frequency_value <- 12  # Monthly data
forecast_horizon <- 12  # Forecast horizon of 12 months

# Example start and end date for financial data
start_date <- "2023-01-01"
end_date <- "2023-12-31"

# Load necessary libraries
library(stats)

# Convert data to time series object
ts_data <- ts(df$value, start = c(year_start, month_start), frequency = 12)

# Perform time series decomposition
ts_decomposition <- decompose(ts_data)

# Plot time series components
plot(ts_decomposition)

# Forecast future values
forecast_model <- forecast::forecast(ts_data, h = forecast_horizon)
plot(forecast_model)

# correlation
data(iris)

# remove Species column
data <- select(iris,-Species)

# calculate corelation
print(cor(data))

# calculate covariance
print(cov(data))
